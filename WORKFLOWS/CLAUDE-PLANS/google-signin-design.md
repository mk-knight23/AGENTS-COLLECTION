# Google Sign-In with Session Persistence Design

**Goal:** Implement Google Sign-In for all job portals using session persistence - manual one-time login with Gmail (kazimusharraf1234@gmail.com), then reuse saved browser sessions.

**Architecture:** Playwright automation that clicks "Sign in with Google" on each portal, completes OAuth flow once, saves browser context (cookies + localStorage), and reloads sessions on subsequent runs.

## How It Works

1. **First Run (Setup Mode)**:
   - User runs: `python -m mjas setup-sessions --visible`
   - Opens browser for each portal
   - Clicks "Sign in with Google" button
   - User completes Google OAuth manually (one-time)
   - Saves Playwright browser context to `data/sessions/{portal}.json`

2. **Subsequent Runs**:
   - Loads saved browser context from session files
   - Skips login entirely
   - Directly starts job search/application

## Components

1. **SessionManager** - Save/load browser contexts
2. **Modified PortalWorker** - Load session on start
3. **Setup Sessions CLI** - New command: `setup-sessions`
4. **Updated Portal Classes** - Click "Sign in with Google"

## Cleanup

Remove:
- config/credentials.env and encrypted files
- Password fields in portals
- CredentialVault (simplify)
- Password setup scripts
