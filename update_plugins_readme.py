import httpx
import json
import pathlib
import re
import os

root = pathlib.Path(__file__).parent.resolve()

TOKEN = os.environ.get("GITHUB_TOKEN", "")


def replace_chunk(content, marker, chunk, inline=False):
    """Replace content between marker comments."""
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)


def extract_repo_info(url):
    """Extract owner and repo name from GitHub URL."""
    # https://github.com/soderlind/repo-name -> (soderlind, repo-name)
    parts = url.rstrip("/").split("/")
    return parts[-2], parts[-1]


def fetch_repo_info(owner, repo, token):
    """Fetch repository description and stars from GitHub API."""
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    headers["Accept"] = "application/vnd.github.v3+json"
    
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = httpx.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "description": data.get("description", "") or "",
            "stars": data.get("stargazers_count", 0)
        }
    return {"description": "", "stars": 0}


def format_repo_name(repo_name):
    """Format repo name for display (replace hyphens with spaces, title case)."""
    return repo_name.replace("-", " ").title()


def generate_html_table(repos):
    """Generate HTML table with two columns of dl/dt/dd elements."""
    rows = []
    
    for i in range(0, len(repos), 2):
        row_cells = []
        
        for j in range(2):
            if i + j < len(repos):
                repo = repos[i + j]
                stars = repo.get("stars", 0)
                stars_text = f" ⭐ {stars}" if stars > 0 else ""
                cell = (
                    f'<dl>\n'
                    f'<dt><a href="{repo["url"]}">{repo["name"]}</a>{stars_text}</dt>\n'
                    f'<dd>{repo["description"]}</dd>\n'
                    f'</dl>'
                )
                row_cells.append(f'<td valign="top" width="50%">\n{cell}\n</td>')
            else:
                row_cells.append('<td></td>')
        
        rows.append(f'<tr>\n{row_cells[0]}\n{row_cells[1]}\n</tr>')
    
    return '<table>\n' + '\n'.join(rows) + '\n</table>'


def main():
    # Read repo.json
    repo_json_path = root / "repo.json"
    with open(repo_json_path) as f:
        repo_data = json.load(f)
    
    # Process each repo
    repos = []
    for item in repo_data:
        url = item["url"]
        owner, repo_name = extract_repo_info(url)
        
        # Fetch repo info from API (description and stars)
        print(f"Fetching info for {owner}/{repo_name}...")
        repo_info = fetch_repo_info(owner, repo_name, TOKEN)
        
        # Use description from JSON if provided, otherwise use API response
        description = item.get("description", "").strip()
        if not description:
            description = repo_info["description"]
        
        repos.append({
            "url": url,
            "name": format_repo_name(repo_name),
            "description": description or "No description available.",
            "stars": repo_info["stars"],
        })
    
    # Generate HTML table
    html_table = generate_html_table(repos)
    
    # Update README.md
    readme_path = root / "README.md"
    readme_contents = readme_path.read_text()
    
    rewritten = replace_chunk(readme_contents, "plugins", html_table)
    readme_path.write_text(rewritten)
    
    print(f"Updated README.md with {len(repos)} plugins.")


if __name__ == "__main__":
    main()
