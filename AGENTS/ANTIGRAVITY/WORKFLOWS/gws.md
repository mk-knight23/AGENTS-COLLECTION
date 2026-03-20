---
description: Universal Google Workspace CLI (gws) command reference and skill discovery
---

# /gws

One CLI for all of Google Workspace. Use this workflow to manage Drive, Gmail, Calendar, Sheets, Docs, Chat, and more via `gws`.

## Prerequisites

Check if `gws` is installed:

```bash
gws --version || echo "gws not found"
```

If not found, install it:

```bash
npm install -g @googleworkspace/cli
```

## Authentication

| Task | Command |
| :--- | :--- |
| **Setup Project** | `gws auth setup` |
| **Login** | `gws auth login` |
| **Login (Scopes)** | `gws auth login -s drive,gmail,sheets` |
| **Export Creds** | `gws auth export --unmasked` |

## Common Operations

### Google Drive
```bash
# List files
gws drive files list --params '{"pageSize": 10}'
# Upload file
gws drive files create --json '{"name": "Report"}' --upload ./report.pdf
```

### Gmail
```bash
# List messages
gws gmail users messages list --params '{"userId": "me", "maxResults": 5}'
# Get thread
gws gmail users threads get --params '{"userId": "me", "id": "THREAD_ID"}'
```

### Google Sheets
```bash
# Create spreadsheet
gws sheets spreadsheets create --json '{"properties": {"title": "New Sheet"}}'
# Read values (Note: Use single quotes for ranges with !)
gws sheets spreadsheets values get --params '{"spreadsheetId": "ID", "range": "Sheet1!A1:C10"}'
```

## Skill Discovery

Every API module has a corresponding skill. If the user asks for advanced automation, search for related skills:

```bash
# Search for gws skills
ls -F /Users/mkazi/.gemini/antigravity/skills/ | grep gws-
```

## Usage Guidelines

1. **Structured JSON**: Every `gws` response is JSON. Use `jq` or Python for processing if needed.
2. **Schema Inspection**: Use `gws schema <svc.res.meth>` to find exact parameters.
3. **Dry Runs**: Use `--dry-run` to preview a request without executing it.
4. **Shell Escaping**: Always wrap `--params` and `--json` in single quotes to avoid shell interference.
