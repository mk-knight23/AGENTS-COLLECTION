---
name: gws
description: Google Workspace CLI for managing Gmail, Sheets, Calendar, and Drive from the command line.
homepage: https://github.com/googleapis/google-workspace-cli
metadata: {"nanobot":{"emoji":"📧","requires":{"bins":["gws"]}}}
---

# Google Workspace CLI (gws)

**Powerful command-line interface for Google Workspace services**

---

## 🚀 Overview

The `gws` CLI provides a unified interface to interact with Google Workspace services directly from your terminal:
- 📧 **Gmail** - Manage emails, labels, filters
- 📊 **Sheets** - Read/write spreadsheets, data manipulation
- 📅 **Calendar** - Events, scheduling, reminders
- 📁 **Drive** - File operations, sharing, permissions

Perfect for automation scripts, batch operations, and integration with nanobot workflows.

---

## 📦 Installation

### Prerequisites
```bash
# Python 3.8+ required
python3 --version

# Install via pip
pip3 install google-workspace-cli

# Or install from source
git clone https://github.com/googleapis/google-workspace-cli.git
cd google-workspace-cli
pip3 install -e .
```

### Quick Setup
```bash
# Initialize gws (interactive wizard)
gws init

# Verify installation
gws --version
gws --help
```

---

## 🔐 OAuth Authentication

### 1. Create Google Cloud Project
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable required APIs:
   - Gmail API
   - Google Sheets API
   - Google Calendar API
   - Google Drive API

### 2. Create OAuth Credentials
```bash
# Navigate to APIs & Services → Credentials
# Create OAuth 2.0 Client ID
# Application type: Desktop app
# Download credentials JSON file
```

### 3. Configure gws
```bash
# Set credentials file path
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="/path/to/credentials.json"

# Run authentication flow
gws auth login

# Grant permissions for each API scope:
# - gmail.readonly, gmail.modify, gmail.send
# - spreadsheets.readonly, spreadsheets
# - calendar.readonly, calendar.events
# - drive.readonly, drive
```

### 4. Verify Authentication
```bash
# Test Gmail connection
gws gmail profile

# Test Sheets connection
gws sheets list

# Test Calendar connection
gws calendars list

# Test Drive connection
gws drive files list --limit 5
```

---

## 📧 Gmail Usage

### Read Emails
```bash
# List recent emails (default: 10)
gws gmail messages list

# List with filters
gws gmail messages list --max-results 20 --query "is:unread"

# Search emails
gws gmail messages list --query "from:hr@company.com"

# Get specific email
gws gmail messages get MESSAGE_ID

# Get email body only
gws gmail messages get MESSAGE_ID --format=raw | jq -r '.payload.body.data' | base64 -d
```

### Send Emails
```bash
# Send simple email
gws gmail messages send --to "recipient@example.com" \
  --subject "Meeting Update" \
  --body "Hello, meeting rescheduled to 3 PM."

# Send email with attachments
gws gmail messages send --to "team@company.com" \
  --subject "Report" \
  --body "Please find attached report." \
  --attach "/path/to/report.pdf"

# Send HTML email
gws gmail messages send --to "client@example.com" \
  --subject "Welcome" \
  --html-body "<h1>Welcome!</h1><p>Thanks for joining us.</p>"
```

### Manage Labels
```bash
# List labels
gws gmail labels list

# Create label
gws gmail labels create "HR/Pending"

# Apply label to email
gws gmail messages modify MESSAGE_ID --add-labels "HR/Pending"
```

### Filters and Automation
```bash
# Create filter for HR emails
gws gmail filters create --from "hr@company.com" \
  --apply-label "HR/Inbox"

# List filters
gws gmail filters list
```

---

## 📊 Sheets Usage

### List Spreadsheets
```bash
# List all spreadsheets
gws sheets list

# List with search
gws sheets list --query "employee"
```

### Read Data
```bash
# Get spreadsheet metadata
gws spreadsheets get SPREADSHEET_ID

# Read specific range
gws spreadsheets values get SPREADSHEET_ID --range "Sheet1!A1:Z100"

# Read first sheet
gws spreadsheets values get SPREADSHEET_ID --range "Sheet1"

# Export to CSV
gws spreadsheets values get SPREADSHEET_ID --range "Sheet1" > data.csv
```

### Write Data
```bash
# Update single cell
gws spreadsheets values update SPREADSHEET_ID \
  --range "Sheet1!A1" \
  --value "Updated Value"

# Batch update (from file)
gws spreadsheets values batch-update SPREADSHEET_ID \
  --input-data data.json

# Append row
gws spreadsheets values append SPREADSHEET_ID \
  --range "Sheet1!A:Z" \
  --value "John,Doe,Engineering,Senior Engineer"

# Clear range
gws spreadsheets values clear SPREADSHEET_ID --range "Sheet1!A2:Z1000"
```

### Create and Manage
```bash
# Create new spreadsheet
gws spreadsheets create --title "Employee Database"

# Duplicate sheet
gws spreadsheets sheets copy SPREADSHEET_ID --sheet-id 0

# Delete sheet
gws spreadsheets sheets delete SPREADSHEET_ID --sheet-id 1
```

---

## 📅 Calendar Usage

### List Calendars
```bash
# List all calendars
gws calendars list

# List events in default calendar
gws calendars events list

# List events for specific calendar
gws calendars events list --calendar-id "primary"

# List events in date range
gws calendars events list \
  --time-min "2026-03-01T00:00:00Z" \
  --time-max "2026-03-31T23:59:59Z"
```

### Create Events
```bash
# Create simple event
gws calendars events create \
  --summary "Team Meeting" \
  --start "2026-03-10T14:00:00" \
  --end "2026-03-10T15:00:00"

# Create with details
gws calendars events create \
  --summary "Project Review" \
  --description "Review Q1 progress" \
  --location "Conference Room A" \
  --start "2026-03-10T10:00:00" \
  --end "2026-03-10T11:30:00" \
  --attendees "alice@example.com,bob@example.com" \
  --send-notifications

# Create recurring event
gws calendars events create \
  --summary "Weekly Standup" \
  --start "2026-03-10T09:00:00" \
  --end "2026-03-10T09:30:00" \
  --recurrence "RRULE:FREQ=WEEKLY;BYDAY=MO,WE,FR"
```

### Manage Events
```bash
# Get event details
gws calendars events get EVENT_ID

# Update event
gws calendars events update EVENT_ID \
  --summary "Updated Meeting" \
  --start "2026-03-10T15:00:00" \
  --end "2026-03-10T16:00:00"

# Delete event
gws calendars events delete EVENT_ID

# Quick add (natural language)
gws calendars events quick-add \
  --text "Meeting with John tomorrow at 2pm"
```

---

## 📁 Drive Usage

### List Files
```bash
# List files in root
gws drive files list

# List with search
gws drive files list --query "name contains 'report'"

# List by folder
gws drive files list --query "'FOLDER_ID' in parents"

# List in trash
gws drive files list --query "trashed = true"
```

### File Operations
```bash
# Upload file
gws drive files upload --file "/path/to/document.pdf" \
  --name "Q1 Report.pdf"

# Download file
gws drive files download FILE_ID --output "/path/to/local.pdf"

# Copy file
gws drive files copy FILE_ID --name "Copy of Document.pdf"

# Move file to folder
gws drive files update FILE_ID \
  --add-parents "FOLDER_ID" \
  --remove-parents "OLD_FOLDER_ID"

# Delete file (to trash)
gws drive files delete FILE_ID

# Permanently delete
gws drive files delete FILE_ID --permanent
```

### Sharing and Permissions
```bash
# Share file
gws drive permissions create FILE_ID \
  --email "colleague@example.com" \
  --role "writer"

# Share with link
gws drive permissions create FILE_ID \
  --role "reader" \
  --type "anyone"

# List permissions
gws drive permissions list FILE_ID

# Remove permission
gws drive permissions delete FILE_ID PERMISSION_ID

# Create shareable link
gws drive files get FILE_ID --fields="webViewLink"
```

### Folders
```bash
# Create folder
gws drive files create --name "Project Files" --mimeType "application/vnd.google-apps.folder"

# Create folder in parent
gws drive files create --name "2026 Reports" \
  --mimeType "application/vnd.google-apps.folder" \
  --parents "PARENT_FOLDER_ID"

# Get folder contents
gws drive files list --query "'FOLDER_ID' in parents and trashed=false"
```

---

## 🤖 Nanobot Integration

### In nanobot Prompts
```nanobot
# Check for new HR emails
gws gmail messages list --max-results 5 --query "from:hr@company.com is:unread"

# Create calendar event from extracted info
gws calendars events create --summary "$EVENT_TITLE" --start "$START_TIME" --end "$END_TIME"

# Update employee database in Sheets
gws spreadsheets values append $SPREADSHEET_ID --range "Sheet1!A:Z" --value "$EMPLOYEE_DATA"

# Upload report to Drive
gws drive files upload --file "$REPORT_PATH" --name "$REPORT_NAME"
```

### Workflow Example
```bash
#!/bin/bash
# Automated HR Email Processing

SPREADSHEET_ID="1BxiMVs0XRA5nFMdKvBdBZjGMUUqpt35..."
DRIVE_FOLDER_ID="0BxXXXXXXXXXXXXXXXXXXXX"

# Get unread HR emails
EMAILS=$(gws gmail messages list --query "from:hr@company.com is:unread" --format=json)

# Process each email
echo "$EMAILS" | jq -r '.[].id' | while read -r MSG_ID; do
  # Extract email details
  SUBJECT=$(gws gmail messages get $MSG_ID --format=json | jq -r '.snippet')
  BODY=$(gws gmail messages get $MSG_ID --format=raw | jq -r '.payload.body.data' | base64 -d)
  
  # Parse and extract data (using your parsing logic)
  EMPLOYEE_DATA=$(echo "$BODY" | parse_employee_email)
  
  # Update spreadsheet
  gws spreadsheets values append $SPREADSHEET_ID \
    --range "Sheet1!A:Z" \
    --value "$EMPLOYEE_DATA"
  
  # Mark as processed
  gws gmail messages modify $MSG_ID --add-labels "HR/Processed"
done
```

### Environment Variables for Nanobot
```bash
# Add to .env or nanobot config
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="${HOME}/.config/gws/credentials.json"
export GOOGLE_WORKSPACE_CLI_CONFIG_DIR="${HOME}/.config/gws"
export GOOGLE_WORKSPACE_CLI_SPREADSHEET_ID="your-sheet-id"
export GOOGLE_WORKSPACE_CLI_CALENDAR_ID="primary"
export GOOGLE_WORKSPACE_CLI_DRIVE_FOLDER_ID="your-folder-id"
```

---

## 🔒 Security Best Practices

### Credential Management
1. **Never commit credentials to version control**
   ```bash
   # Add to .gitignore
   echo "*.json" >> .gitignore
   echo "credentials.json" >> .gitignore
   ```

2. **Use environment variables** for credential paths
   ```bash
   export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="/secure/path/credentials.json"
   ```

3. **Restrict API scopes** - Only request necessary permissions
   - Use `gmail.readonly` instead of `gmail.modify` when possible
   - Limit to specific calendars/drives

4. **Use service accounts for automation**
   ```bash
   # Create service account in Google Cloud Console
   # Download service account JSON key
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
   ```

### Access Control
```bash
# Enable app-level password restrictions
# Settings → Security → App passwords

# Use 2FA for Google account
# Create dedicated service account for automation

# Set up audit logging
# Google Admin Console → Security → Audit logs
```

### Data Sanitization
```bash
# Set sanitize template for sensitive data
export GOOGLE_WORKSPACE_CLI_SANITIZE_TEMPLATE="templates/sanitize.txt"

# Example sanitize.txt:
# REDACT_EMAIL: [email redacted]
# REDACT_PHONE: [phone redacted]
# REDACT_SSN: [SSN redacted]
```

### Rotation and Expiry
```bash
# Rotate credentials every 90 days
# Monitor OAuth consent screen for unauthorized apps
# Revoke unused credentials regularly
```

---

## 📊 Monitoring and Automation

### Email Monitoring Script
```bash
# Monitor for specific email patterns
watch -n 300 'gws gmail messages list --query "is:unread from:hr@company.com"'
```

### Scheduled Tasks
```bash
# Add to crontab for periodic checks
# Check for urgent emails every 10 minutes
*/10 * * * * gws gmail messages list --query "is:urgent is:unread" | send_alert

# Daily calendar sync
0 8 * * * gws calendars events list --time-min="$(date -u +%Y-%m-%dT00:00:00Z)" > /tmp/today_events.txt

# Weekly backup
0 0 * * 0 gws drive files list --format=json > /tmp/drive_backup_$(date +%Y%m%d).json
```

---

## 🐛 Troubleshooting

### Authentication Issues
```bash
# Clear cached credentials
rm -rf ~/.config/gws/token.json

# Re-authenticate
gws auth login

# Check credential permissions
gws auth list
```

### API Quota Exceeded
```bash
# Check quota usage
gws quota --service=gmail

# Implement exponential backoff in scripts
sleep $((2 ** RETRY_COUNT))
```

### File Not Found
```bash
# Verify file ID
gws drive files get FILE_ID

# Check trash
gws drive files list --query "trashed=true and name='myfile.pdf'"
```

---

## 📚 Resources

- [Official Documentation](https://developers.google.com/workspace)
- [gws CLI GitHub](https://github.com/googleapis/google-workspace-cli)
- [Google Cloud Console](https://console.cloud.google.com/)
- [API Reference](https://developers.google.com/workspace/guides)

---

**Version:** 1.0.0  
**Status:** Production Ready  
**Security:** Requires OAuth 2.0 authentication
