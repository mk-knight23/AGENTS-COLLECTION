# Security Policy

## Supported Versions
We prioritize the latest production release.

## Reporting a Vulnerability
Please do not report security vulnerabilities through public GitHub issues. Instead, contact the maintainer through the channel specified in the project profile.

### Production Hardening
- **Secrets Management**: Do not commit keys. Use environment variables.
- **Dependency Tracking**: Automated scans via Snyk/GitHub are enabled.
- **Audit**: All PRs undergo automated security analysis.
