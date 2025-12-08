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
    """Fetch repository description, stars and creation date from GitHub API."""
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
            "stars": data.get("stargazers_count", 0),
            "created_at": data.get("created_at", "")
        }
    return {"description": "", "stars": 0, "created_at": ""}


def format_repo_name(repo_name):
    """Format repo name for display (replace hyphens with spaces, title case)."""
    return repo_name.replace("-", " ").title()


def generate_html_table(repos):
    """Generate HTML table with two columns of dl/dt/dd elements.
    Newest repo (is_new) is promoted to a top row spanning both columns with enhanced styling.
    Adds ⭐ star count (if >0) and 🚀 rocket for the newest repo.
    """
    rows = []

    # Separate newest repo from the rest
    newest_repo = None
    other_repos = []
    for repo in repos:
        if repo.get("is_new"):
            newest_repo = repo
        else:
            other_repos.append(repo)

    # Helper to build cell HTML for regular repos
    def build_cell(repo):
        stars = repo.get("stars", 0)
        stars_text = f" ⭐ {stars}" if stars > 0 else ""
        return (
            f'<dl>\n'
            f'<dt><a href="{repo["url"]}#readme">{repo["name"]}</a>{stars_text}</dt>\n'
            f'<dd>{repo["description"]}</dd>\n'
            f'</dl>'
        )

    # Enhanced promo row for newest repo with bold heading, rocket, and separator
    if newest_repo:
        stars = newest_repo.get("stars", 0)
        stars_text = f" ⭐ {stars}" if stars > 0 else ""
        promo_html = (
            f'<h3>🚀 <a href="{newest_repo["url"]}#readme">{newest_repo["name"]}</a>{stars_text}</h3>\n'
            f'<p>{newest_repo["description"]}</p>'
        )
        rows.append(
            f'<tr>\n<td colspan="2">\n\n{promo_html}\n\n<hr>\n</td>\n</tr>'
        )

    # Remaining repos in two-column layout
    for i in range(0, len(other_repos), 2):
        row_cells = []
        for j in range(2):
            if i + j < len(other_repos):
                repo = other_repos[i + j]
                cell = build_cell(repo)
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
    created_dates = []
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
        
        # Compute age to decide if new (<30 days)
        created_at = repo_info.get("created_at", "")
        is_new = False
        created_dt = None
        if created_at:
            # created_at example: 2025-11-05T12:34:56Z
            try:
                from datetime import datetime, timezone
                created_dt = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                created_dates.append(created_dt)
            except Exception:
                is_new = False

        repos.append({
            "url": url,
            "name": format_repo_name(repo_name),
            "description": description or "No description available.",
            "stars": repo_info["stars"],
            "is_new": is_new,
            "_created_dt": created_dt,
        })

    # Mark only the single newest repo with rocket
    try:
        newest_dt = None
        for r in repos:
            if r.get("_created_dt") is not None:
                if newest_dt is None or r["_created_dt"] > newest_dt:
                    newest_dt = r["_created_dt"]
        if newest_dt is not None:
            # Clear all is_new flags, then set only the newest
            for r in repos:
                r["is_new"] = False
            for r in repos:
                if r.get("_created_dt") == newest_dt:
                    r["is_new"] = True
                    break
    except Exception:
        pass
    
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
