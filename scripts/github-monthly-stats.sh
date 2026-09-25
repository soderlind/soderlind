#!/usr/bin/env bash
# Monthly GitHub stats: commits authored + distinct repos contributed to.
#
# Usage: scripts/github-monthly-stats.sh [username] [months]
#   username  GitHub login to report on   (default: soderlind)
#   months    Number of months to report  (default: 12, ending this month)
#
# Requires: gh (authenticated: `gh auth login`).
#
# Notes:
#   - totalCommitContributions counts commits authored (not issues/PRs/reviews).
#   - totalRepositoriesWithContributedCommits = distinct repos committed to.
#   - Only contributions GitHub attributes to the account are counted; private
#     repos require token access + "Include private contributions" enabled.
set -euo pipefail

USER="${1:-soderlind}"
MONTHS="${2:-12}"

# Build one batched GraphQL query with an aliased window per month.
fields=""
for ((i = MONTHS - 1; i >= 0; i--)); do
  # First day of the month, i months ago (portable macOS + GNU date).
  if date -v-1m +%Y >/dev/null 2>&1; then
    start=$(date -u -v-"${i}"m +%Y-%m-01) # BSD/macOS
    end=$(date -u -v-"${i}"m -v+1m +%Y-%m-01)
  else
    start=$(date -u -d "$(date -u +%Y-%m-01) -${i} month" +%Y-%m-01) # GNU
    end=$(date -u -d "$(date -u +%Y-%m-01) -${i} month +1 month" +%Y-%m-01)
  fi
  alias="m${start//-/_}"
  fields+="${alias}: contributionsCollection(from: \"${start}T00:00:00Z\", to: \"${end}T00:00:00Z\") { totalCommitContributions totalRepositoriesWithContributedCommits } "
done

query="query(\$login: String!) { user(login: \$login) { ${fields} } }"

printf 'Month     Commits  Repos\n'
printf -- '-------   -------  -----\n'
gh api graphql -f query="$query" -F login="$USER" --jq '
  .data.user
  | to_entries
  | sort_by(.key)
  | .[]
  | "\(.key | ltrimstr("m") | gsub("_";"-") | .[0:7])   \(.value.totalCommitContributions)\t \(.value.totalRepositoriesWithContributedCommits)"
'
