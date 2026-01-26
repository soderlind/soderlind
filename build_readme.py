import httpx
import json
import pathlib
import re
import os

root = pathlib.Path(__file__).parent.resolve()
TOKEN = os.environ.get("SODERLIND_TOKEN", "")


def replace_chunk(content, marker, chunk, inline=False):
	r = re.compile(
		r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
		re.DOTALL,
	)
	if not inline:
		chunk = "\n{}\n".format(chunk)
	chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(
		marker, chunk, marker)
	return r.sub(chunk, content)


def get_repo_info(url):
	"""Fetch repo info from GitHub API (stars, description)."""
	# Extract owner/repo from URL
	parts = url.rstrip('/').split('/')
	owner, repo = parts[-2], parts[-1]
	api_url = f"https://api.github.com/repos/{owner}/{repo}"
	
	headers = {}
	if TOKEN:
		headers["Authorization"] = f"Bearer {TOKEN}"
	
	try:
		response = httpx.get(api_url, timeout=10, headers=headers)
		if response.status_code == 200:
			data = response.json()
			return {
				"stars": data.get("stargazers_count", 0),
				"description": data.get("description", ""),
				"name": data.get("name", repo),
			}
	except Exception:
		pass
	
	return {"stars": 0, "description": "", "name": repo}


def get_title_from_repo(url, custom_title=None):
	"""Get display title from custom title or repo name."""
	if custom_title:
		return custom_title
	# Extract repo name and convert to title case
	repo_name = url.rstrip('/').split('/')[-1]
	return repo_name.replace('-', ' ').title()


def load_plugins():
	"""Load plugins from repo.json."""
	repo_json = root / "repo.json"
	with repo_json.open() as f:
		return json.load(f)


def build_markdown(plugins):
	"""Build the markdown table with parent/child structure."""
	md_parts = []
	md_parts.append("")
	md_parts.append("<table>")
	
	for parent in plugins:
		# Get parent repo info (only if URL exists)
		parent_url = parent.get("url")
		if parent_url:
			parent_info = get_repo_info(parent_url)
			parent_title = get_title_from_repo(parent_url, parent.get("title"))
			parent_desc = parent.get("description") or parent_info["description"]
			parent_stars = parent_info["stars"]
		else:
			parent_title = parent.get("title", "Plugins")
			parent_desc = parent.get("description", "")
			parent_stars = 0
		
		# Parent row (full width)
		stars_display = f" ⭐ {parent_stars}" if parent_stars > 0 else ""
		md_parts.append("<tr>")
		md_parts.append('<td colspan="2">')
		md_parts.append("")
		if parent_url:
			md_parts.append(f'### <a href="{parent_url}#readme">{parent_title}</a>{stars_display}')
		else:
			md_parts.append(f'### {parent_title}')
		md_parts.append("")
		if parent_desc:
			md_parts.append(f"{parent_desc}")
			md_parts.append("")
		md_parts.append("</td>")
		md_parts.append("</tr>")
		
		# Children in two columns (sorted alphabetically by title)
		children = parent.get("children", [])
		children = sorted(children, key=lambda c: get_title_from_repo(c["url"], c.get("title")).lower())
		for i in range(0, len(children), 2):
			md_parts.append("<tr>")
			
			# Left column
			child = children[i]
			child_info = get_repo_info(child["url"])
			child_title = get_title_from_repo(child["url"], child.get("title"))
			child_desc = child.get("description") or child_info["description"]
			child_stars = child_info["stars"]
			stars_display = f" ⭐ {child_stars}" if child_stars > 0 else ""
			
			md_parts.append('<td valign="top" width="50%">')
			md_parts.append("")
			md_parts.append(f'**<a href="{child["url"]}#readme">{child_title}</a>**{stars_display}')
			md_parts.append("")
			if child_desc:
				md_parts.append(f"{child_desc}")
				md_parts.append("")
			md_parts.append("</td>")
			
			# Right column (if exists)
			if i + 1 < len(children):
				child = children[i + 1]
				child_info = get_repo_info(child["url"])
				child_title = get_title_from_repo(child["url"], child.get("title"))
				child_desc = child.get("description") or child_info["description"]
				child_stars = child_info["stars"]
				stars_display = f" ⭐ {child_stars}" if child_stars > 0 else ""
				
				md_parts.append('<td valign="top" width="50%">')
				md_parts.append("")
				md_parts.append(f'**<a href="{child["url"]}#readme">{child_title}</a>**{stars_display}')
				md_parts.append("")
				if child_desc:
					md_parts.append(f"{child_desc}")
					md_parts.append("")
				md_parts.append("</td>")
			else:
				md_parts.append('<td valign="top" width="50%"></td>')
			
			md_parts.append("</tr>")
	
	md_parts.append("</table>")
	md_parts.append("")
	return "\n".join(md_parts)


if __name__ == "__main__":
	readme = root / "README.md"
	plugins = load_plugins()
	md = build_markdown(plugins)
	readme_contents = readme.open().read()
	rewritten = replace_chunk(readme_contents, "plugins", md)
	readme.open("w").write(rewritten)

	readme.open("w").write(rewritten)
