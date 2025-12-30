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
    """Fetch repository name, description, stars and creation date from GitHub API."""
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    headers["Accept"] = "application/vnd.github.v3+json"
    
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = httpx.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data.get("name", repo),
            "description": data.get("description", "") or "",
            "stars": data.get("stargazers_count", 0),
            "created_at": data.get("created_at", "")
        }
    return {"name": repo, "description": "", "stars": 0, "created_at": ""}


def format_repo_name(repo_name):
    """Format repo name for display (replace hyphens with spaces, smart title case with acronym handling)."""
    # Common acronyms to preserve in uppercase when they are standalone words.
    acronyms = {
        "wp",
        "ai",
        "api",
        "css",
        "js",
        "html",
        "php",
        "sql",
        "url",
        "http",
        "https",
        "xml",
        "json",
        "rest",
        "ajax",
        "cdn",
        "ssl",
        "seo",
        "ui",
        "ux",
    }

    words = repo_name.replace("-", " ").split()
    formatted_words = []
    for word in words:
        lower_word = word.lower()
        if lower_word in acronyms:
            formatted_words.append(word.upper())
            continue

        formatted_word = word.capitalize()
        # Special-case: ensure "wp" inside a word stays uppercase (e.g., passwp -> PassWP).
        formatted_word = re.sub(r"wp", "WP", formatted_word, flags=re.IGNORECASE)
        formatted_words.append(formatted_word)

    return " ".join(formatted_words)


def generate_html_table(repos):
    """Generate HTML table with two columns of dl/dt/dd elements.
    Promoted repo (is_promoted) is promoted to a top row spanning both columns with enhanced styling.
    Adds ⭐ star count (if >0) and 🚀 rocket for the promoted repo.
    """
    rows = []

    # Separate promoted repo from the rest
    promoted_repo = None
    other_repos = []
    for repo in repos:
        if repo.get("is_promoted"):
            promoted_repo = repo
        else:
            other_repos.append(repo)

    # Sort all non-promoted repos alphabetically (display name), case-insensitive.
    other_repos.sort(key=lambda r: (r.get("name") or "").casefold())

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

    # Enhanced promo row for promoted repo with bold heading, rocket, and separator
    if promoted_repo:
        stars = promoted_repo.get("stars", 0)
        stars_text = f" ⭐ {stars}" if stars > 0 else ""
        promo_html = (
            f'<h3>🚀 <a href="{promoted_repo["url"]}#readme">{promoted_repo["name"]}</a>{stars_text}</h3>\n'
            f'<p>{promoted_repo["description"]}</p>'
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
    promoted_url = None
    for item in repo_data:
        # Allow either key name; keep it simple for hand-editing.
        if item.get("promoted") is True or item.get("promote") is True:
            promoted_url = item.get("url")
            break

    for item in repo_data:
        url = item["url"]
        owner, repo_name = extract_repo_info(url)
        
        # Fetch repo info from API (description and stars)
        print(f"Fetching info for {owner}/{repo_name}...")
        repo_info = fetch_repo_info(owner, repo_name, TOKEN)
        
        # Use title from JSON if provided, otherwise format the repo name
        title = item.get("title", "").strip()
        if not title:
            title = format_repo_name(repo_info["name"])
        
        # Use description from JSON if provided, otherwise use API response
        description = item.get("description", "").strip()
        if not description:
            description = repo_info["description"]
        
        # Read created_at (used only for fallback promotion when no repo.json flag is set)
        created_at = repo_info.get("created_at", "")
        created_dt = None
        if created_at:
            # created_at example: 2025-11-05T12:34:56Z
            try:
                from datetime import datetime, timezone
                created_dt = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            except Exception:
                created_dt = None

        repos.append({
            "url": url,
            "name": title,
            "description": description or "No description available.",
            "stars": repo_info["stars"],
            "is_promoted": False,
            "_created_dt": created_dt,
        })

    # Mark a single promoted repo.
    # Priority:
    # 1) repo.json item marked with { "promoted": true } (or "promote": true)
    # 2) fallback: newest repo by created_at
    if promoted_url:
        for r in repos:
            if r.get("url") == promoted_url:
                r["is_promoted"] = True
                break
    else:
        try:
            newest_dt = None
            for r in repos:
                if r.get("_created_dt") is not None:
                    if newest_dt is None or r["_created_dt"] > newest_dt:
                        newest_dt = r["_created_dt"]
            if newest_dt is not None:
                for r in repos:
                    if r.get("_created_dt") == newest_dt:
                        r["is_promoted"] = True
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
