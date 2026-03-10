# Start All Claw Project Gateways (Fix and Retry)

This plan addresses the permission issues encountered when starting the various "Claw" project gateways and restarts all of them from their respective project folders.

## User Review Required

> [!IMPORTANT]
> Some gateways (NanoClaw, PicoClaw) are failing due to macOS `Operation not permitted` errors. I will attempt to bypass these by overriding temporary directories and cache locations. If these continue to fail, it may indicate that the shell environment lacks "Full Disk Access" or similar permissions required for certain system-level operations (like starting `container` or writing to `/var/folders`).

## Proposed Changes

### Environment Configuration

- **PicoClaw**:
  - Set `GOCACHE` and `GOTMPDIR` to a local folder within the project (`~/Open-Universe/picoclaw/.cache`) to avoid `/var/folders` permission errors.
- **NanoClaw**:
  - Investigate `container` tool environment variables to see if the `apiserver.plist` path can be overridden.
- **ZeroClaw**:
  - Ensure the log directory `~/.zeroclaw/logs` has correct permissions.

---

### Startup Orchestration

#### [MODIFY] [task.md](file:///Users/mkazi/.gemini/antigravity/brain/031bbd31-0190-442e-869b-49e3585e2291/task.md)
Update the task list to reflect the fix and retry strategy.

---

## Verification Plan

### Automated Verification
- **Port Check**: Use `lsof -i -P -n | grep LISTEN` to verify that gateways are listening on their expected ports.
- **Log Inspection**: Tail the latest log entries for each project to ensure they didn't crash immediately after startup.
  - `openclaw`: `~/.openclaw/logs/gateway.log`
  - `zeroclaw`: `~/.zeroclaw/zeroclaw.log`
  - `NanoClaw`: `~/Open-Universe/NanoClaw/logs/nanoclaw.log`
  - `picoclaw`: `~/Open-Universe/picoclaw/logs/picoclaw.log`

### Manual Verification
- The user can verify by attempting to interact with the gateways via their respective endpoints (e.g., `http://127.0.0.1:42617` for ZeroClaw).
