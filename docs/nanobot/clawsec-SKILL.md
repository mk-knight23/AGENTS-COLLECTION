# ClawSec Suite Manager

**Advanced Security Suite for Agent Skills**

---

## 🛡️ Overview

ClawSec is a comprehensive security management system that provides:
- 📢 **Advisory Feed Monitoring** - Real-time security advisories (CVE, vendor alerts)
- 🔐 **Cryptographic Signature Verification** - Verify skill integrity before execution
- ⛔ **Approval-Gated Malicious Response** - Detect & block potentially malicious skills
- 🚀 **Guided Setup** - Install and configure additional security skills

---

## 🎯 Use Cases

1. **Security Monitoring**: Track CVE advisories, vendor security alerts
2. **Skill Verification**: Validate cryptographic signatures of skills
3. **Threat Detection**: Identify suspicious skill patterns
4. **Automated Security**: Approval workflow for risky operations
5. **Skill Management**: Discover and install security skills

---

## 🏗️ Components

### 1. Advisory Feed Monitor (`advisory_monitor.py`)
- Monitors CVE database (NVD)
- Tracks vendor security advisories
- GitHub Security Advisories
- Real-time alerts via Telegram/Discord
- Severity classification (CRITICAL, HIGH, MEDIUM, LOW)

### 2. Signature Verifier (`signature_verifier.py`)
- GPG signature verification
- SHA-256 checksum validation
- Integrity checks for skill files
- Trust key management
- Signing workflow

### 3. Malicious Skill Detector (`malicious_detector.py`)
- Pattern matching for suspicious code
- Obfuscation detection
- Network request analysis
- File system access detection
- Command injection detection
- Approval workflow with human review

### 4. Security Skill Manager (`security_skills.py`)
- Discover security skills from ClawHub
- Install security tools
- Configure security settings
- Skill integrity verification

### 5. ClawSec Main (`clawsec.py`)
- Main CLI interface
- Orchestrate all components
- Unified dashboard

---

## 📦 Installation

### Prerequisites
```bash
# Install dependencies
pip3 install cryptography gnupg requests pyyaml

# Install GPG (for signature verification)
brew install gnupg  # macOS
# or
apt install gnupg  # Linux

# Install security tools (optional)
brew install nmap burpsuite metasploit-framework
```

### Setup
```bash
# Initialize ClawSec
cd nanobot/skills/clawsec
python3 clawsec.py init

# Configure settings
python3 clawsec.py config

# Generate signing key
python3 clawsec.py generate-key
```

---

## 🚀 Usage

### Advisory Monitoring
```bash
# Start monitoring (runs continuously)
python3 clawsec.py monitor-advisories

# Check recent CVEs
python3 clawsec.py check-cves

# Get specific CVE details
python3 clawsec.py cve CVE-2024-12345
```

### Signature Verification
```bash
# Verify a skill file
python3 clawsec.py verify /path/to/skill/SKILL.md

# Sign a skill file
python3 clawsec.py sign /path/to/skill/SKILL.md

# Check integrity of all skills
python3 clawsec.py audit-skills
```

### Malicious Detection
```bash
# Scan a skill for potential threats
python3 clawsec.py scan /path/to/skill/

# Enable approval mode (interactive)
python3 clawsec.py enable-approval

# Review blocked skills
python3 clawsec.py review-blocked
```

### Security Skills
```bash
# List available security skills
python3 clawsec.py list-skills

# Install a security skill
python3 clawsec.py install-skill vuln-scanner

# Configure security settings
python3 clawsec.py configure
```

---

## 🔐 Security Architecture

### Approval Workflow

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Skill      │ ──▶ │  Detector    │ ──▶ │  Approval   │
│  Request    │     │  (Auto)      │     │  (Human)    │
└─────────────┘     └──────────────┘     └─────────────┘
                          │                     │
                    ┌─────┴─────┐           ┌───┴─────┐
                    │  Threat   │           │ Approve │
                    │  Score    │           │ /Deny   │
                    └───────────┘           └─────────┘
```

### Threat Scoring

| Pattern | Score | Action |
|---------|-------|--------|
| `eval()` | 40 | Warning |
| `exec()` | 50 | Warning |
| `subprocess.run` | 30 | Warning |
| `requests.get` | 20 | Log |
| `os.system` | 60 | Block |
| `__import__(` | 50 | Warning |
| Base64 encoded | 70 | Block |
| Obfuscated code | 80 | Block |
| Network socket | 40 | Warning |
| File write to system dirs | 50 | Block |

**Total Score ≥ 60** → Approval Required
**Total Score ≥ 80** → Automatic Block

---

## 📊 Advisory Sources

### CVE Database (NVD)
- Source: https://nvd.nist.gov/vuln/data-feeds
- Format: JSON 1.1
- Update Frequency: Every 2 hours
- Severity: CVSS 3.1 scoring

### Vendor Advisories
- GitHub Security Advisories
- Vendor RSS feeds
- Product-specific notifications

### Custom Sources
- Add your own advisory feeds
- Configure webhook notifications
- Set custom severity thresholds

---

## 🔑 Signature System

### GPG Workflow

```bash
# Generate key pair
gpg --full-generate-key

# Export public key
gpg --export --armor > public_key.asc

# Sign a file
gpg --default-key your@email.com --armor --detach-sign file.py

# Verify signature
gpg --verify file.py.sig file.py
```

### Trust Levels

| Level | Description |
|-------|-------------|
| 0 | Unknown - Not signed |
| 1 | Low - Self-signed |
| 2 | Medium - Signed by known developer |
| 3 | High - Signed by trusted authority |
| 4 | Critical - Multi-signed by multiple trusted parties |

---

## 🚨 Alerting

### Supported Channels
- Telegram (via bot)
- Discord (webhook)
- Email (SMTP)
- Local notifications
- Custom webhooks

### Alert Types
- New CVE (CRITICAL/HIGH severity)
- Signature verification failed
- Malicious pattern detected
- Skill integrity compromised
- Approval request pending

---

## 📈 Monitoring Dashboard

```bash
# Show security status
python3 clawsec.py status

# Recent alerts (last 24h)
python3 clawsec.py alerts

# Threat statistics
python3 clawsec.py stats

# Generate report
python3 clawsec.py report --format json
```

---

## 🔧 Configuration

### config.yaml
```yaml
# Advisory Settings
advisories:
  enabled: true
  sources:
    - cve_nvd
    - github_security
  severity_threshold: HIGH
  check_interval_minutes: 120

# Signature Settings
signatures:
  enabled: true
  require_trusted: true
  min_trust_level: 3
  auto_verify: true

# Approval Settings
approval:
  enabled: true
  auto_block_threshold: 80
  auto_approve_safe: true
  notification_channel: telegram

# Monitoring Settings
monitoring:
  log_file: /var/log/clawsec.log
  alert_channels:
    - telegram
    - discord
  retention_days: 90
```

---

## 🎓 Guided Setup

### Interactive Setup
```bash
# Run guided setup
python3 clawsec.py setup
```

**Setup wizard covers:**
1. GPG key generation
2. Trust store initialization
3. Advisory feed configuration
4. Notification setup
5. Approval workflow
6. Security skill installation

### Install Security Skills
```bash
# Vuln Scanner
python3 clawsec.py install-skill vuln-scanner

# Malware Analyzer
python3 clawsec.py install-skill malware-analyzer

# Network Monitor
python3 clawsec.py install-skill net-monitor

# Log Analyzer
python3 clawsec.py install-skill log-analyzer
```

---

## 📚 Skills Integration

### Verified Security Skills

1. **Vuln Scanner** - Scan for known vulnerabilities
2. **Malware Analyzer** - Analyze suspicious files
3. **Network Monitor** - Detect network anomalies
4. **Log Analyzer** - Security log analysis
5. **Threat Intel** - CTI feed integration

All security skills are signed and verified before installation.

---

## 🛡️ Security Best Practices

1. **Always verify signatures** before running new skills
2. **Enable approval mode** for production environments
3. **Keep advisory feeds updated** regularly
4. **Review threat scores** before auto-approving
5. **Audit skills monthly** for integrity
6. **Use trust keys** from verified sources
7. **Enable monitoring** for all security events

---

## 🐛 Troubleshooting

### Issue: Signature verification failed
```bash
# Check if public key is imported
gpg --list-keys

# Import missing key
gpg --import public_key.asc

# Re-verify
python3 clawsec.py verify skill.py
```

### Issue: Malicious detection false positive
```bash
# Add to whitelist
python3 clawsec.py whitelist skill.py

# Review threat rules
python3 clawsec.py rules --list
```

### Issue: Advisory feeds not updating
```bash
# Check network connectivity
python3 clawsec.py test-connectivity

# Clear cache
python3 clawsec.py clear-cache

# Force refresh
python3 clawsec.py refresh-advisories
```

---

## 📖 Related Skills

- **clawhub** - Skill registry and installation
- **github** - GitHub integration
- **tmux** - Session management

---

**Version:** 1.0.0
**Status:** Active Development
**Security Level:** High
