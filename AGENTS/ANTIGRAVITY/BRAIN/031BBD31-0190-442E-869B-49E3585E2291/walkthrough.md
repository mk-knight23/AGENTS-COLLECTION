# Claw Gateways Startup Walkthrough

I have successfully started and verified the gateways for most of the Claw projects. Due to macOS permission restrictions, one gateway requires manual intervention.

## Status Overview

| Project | Status | Port | Log File |
| :--- | :--- | :--- | :--- |
| **OpenClaw** | ✅ Running | `18789` | `~/.openclaw/logs/gateway.log` |
| **ZeroClaw** | ✅ Running | `42617` | `/tmp/zeroclaw.log` |
| **PicoClaw** | ✅ Running | `30191` | `~/Open-Universe/picoclaw/logs/picoclaw.log` |
| **NanoClaw** | ❌ Failed | N/A | `~/Open-Universe/NanoClaw/logs/nanoclaw.log` |

## Detailed Results

### ✅ OpenClaw & ZeroClaw
Both gateways are active and listening on their respective ports. No further action is needed for these.

### ✅ PicoClaw
Initially failed due to permission issues with the default Go cache in `/var/folders/`. I resolved this by overriding the cache directory to a local project folder:
```bash
GOCACHE=$PWD/.cache go build -o picoclaw ./cmd/picoclaw
./picoclaw gateway
```

### ❌ NanoClaw
NanoClaw's container runtime daemon (`container`) is failing to start because it lacks permission to write `apiserver.plist`. This is a system-level security restriction on macOS that cannot be bypassed via environment variables.

**To fix NanoClaw:**
1. Open **System Settings** -> **Privacy & Security** -> **Full Disk Access**.
2. Add your Terminal/iTerm app and grant it Full Disk Access.
3. Manually run `container system start` in your terminal.
4. Restart NanoClaw from the `NanoClaw` folder: `node dist/index.js`.

## Verification Commands
You can check the status of the running gateways with:
```bash
lsof -i -P -n | grep LISTEN | grep -E '18789|42617|30191'
```
