# How the README is Built

The main [README.md](../README.md) is **auto-generated** from data in [repo.json](../repo.json). A Python script reads the JSON, fetches live star counts from GitHub, and writes a formatted HTML table into the README.

## Overview

```
repo.json  ──►  build_readme.py  ──►  README.md
                      │
                GitHub API (star counts, descriptions)
```

1. **repo.json** — you define your repos and how they're grouped.
2. **build_readme.py** — reads `repo.json`, calls the GitHub API for each repo, and builds an HTML `<table>`.
3. **README.md** — the script replaces everything between the marker comments:
   ```html
   <!-- plugins starts -->
   ...generated table...
   <!-- plugins ends -->
   ```
   Content outside those markers is untouched.

## repo.json Syntax

The file is a **JSON array of groups**. Each group becomes a section heading in the table, and its children become two-column rows beneath it.

### Group Object

| Field         | Required | Description                                                                                          |
|---------------|----------|------------------------------------------------------------------------------------------------------|
| `title`       | Yes      | Section heading shown in the README (e.g. `"WordPress Multisite Plugins"`). Supports emoji shortcodes like `:construction:`. |
| `description` | No       | Text displayed below the heading. Can contain HTML. Leave as `""` to omit.                           |
| `url`         | No       | GitHub repo URL for the group itself. If set, the heading becomes a link **and** stars are fetched.   |
| `children`    | No       | Array of child repo objects (see below). Omit or use `[]` for a heading-only row.                    |

### Child Object

| Field         | Required | Description                                                                                                         |
|---------------|----------|---------------------------------------------------------------------------------------------------------------------|
| `url`         | **Yes**  | Full GitHub URL (e.g. `"https://github.com/soderlind/wp-loupe"`).                                                   |
| `title`       | No       | Display name. If omitted, derived from the repo name: hyphens → spaces → Title Case (`wp-loupe` → `"Wp Loupe"`).    |
| `description` | No       | Short description. If omitted or `""`, the repo description is fetched from the GitHub API automatically.           |

### Minimal Example

```json
[
  {
    "title": "My Plugins",
    "description": "A collection of useful plugins.",
    "children": [
      {
        "url": "https://github.com/user/plugin-one"
      },
      {
        "url": "https://github.com/user/plugin-two",
        "title": "Plugin Two",
        "description": "Custom description here."
      }
    ]
  }
]
```

This produces:

| Output                  | Detail                                                        |
|-------------------------|---------------------------------------------------------------|
| **Section heading**     | "My Plugins" with the description underneath                  |
| **plugin-one**          | Title auto-generated as "Plugin One", description from GitHub |
| **Plugin Two**          | Uses the custom title and description                         |

Children are **sorted alphabetically** by title and laid out in a **two-column** grid.

### Group with its own Repo URL

If the group itself is a repo, add `url`:

```json
{
  "title": "Virtual Media Folders",
  "url": "https://github.com/soderlind/virtual-media-folders",
  "description": "Organize your media library into virtual folders.",
  "children": [ ... ]
}
```

The heading becomes a clickable link and the group's star count is shown.

## Running the Build

```bash
# Install dependencies (first time only)
pip install -r requirements.txt

# Set a GitHub token to avoid API rate limits (optional but recommended)
export SODERLIND_TOKEN="ghp_..."

# Rebuild the README
python build_readme.py
```

The script modifies `README.md` **in place** — only the region between the `<!-- plugins starts -->` / `<!-- plugins ends -->` markers is rewritten.

## GitHub Actions Automation

The README is rebuilt automatically by a GitHub Actions workflow defined in [`.github/workflows/update-plugins.yml`](../.github/workflows/update-plugins.yml). It runs in three situations:

| Trigger              | When                                                        |
|----------------------|-------------------------------------------------------------|
| **Push**             | Any commit that changes `repo.json`                         |
| **Schedule (cron)**  | Every day at 07:00 UTC — keeps star counts fresh            |
| **Manual**           | On-demand via the "Run workflow" button in the Actions tab   |

### What the workflow does

1. Checks out the repo.
2. Sets up Python and installs `httpx`.
3. Runs `python build_readme.py` with `GITHUB_TOKEN` so API calls are authenticated.
4. If the README changed, commits and pushes automatically (as `github-actions` bot).

Because of this automation, you typically only need to **edit `repo.json` and push** — the workflow takes care of the rest.

## Tips

- **Empty description** (`""`) → the script fetches the description from the GitHub API.
- **Custom description** → overrides the API description; can contain HTML.
- **No `title` on a child** → title is auto-derived from the repo URL slug.
- **Star counts** are always live from the GitHub API; they are not stored in `repo.json`.
