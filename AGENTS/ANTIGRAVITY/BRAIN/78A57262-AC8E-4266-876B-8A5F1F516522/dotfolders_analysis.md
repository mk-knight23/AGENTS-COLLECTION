# Home Directory Dotfolders (.folders) Analysis

Dotfolders (folders starting with `.`) in your home directory are generally used by applications and tools to store configuration settings, cache files, local installations, and state over time.

Based on the scan of `/Users/mkazi`, here is a grouped breakdown of the dotfolders found on your system:

## 1. Development & IDE Tools
These folders are used by your code editors, AI coding assistants, and IDEs to store configurations, extensions, and AI model contexts.
- **`.vscode`**: Configuration, extensions, and state for Visual Studio Code.
- **`.cursor`**: Configuration and state for the Cursor IDE (an AI-powered VS Code fork).
- **`.claude`**: Settings, rules, and configurations for Claude Code CLI (e.g., anthropic keys, mcp servers).
- **`.roo`**: Configuration for Roo-Code (likely an AI coding assistant).
- **`.cline`**: Configuration for Cline (an AI coding assistant inside VS Code).
- **`.agent-deck`**: Configuration for an AI agent control system (likely related to Claude/Antigravity).
- **`.kiro`, `.kilocode`**: KiloCode configurations and skills (Agentic AI tools).
- **`.codeium`**: Codeium AI assistant local data and binaries.
- **`.codex`**: Likely related to OpenAI Codex or a similar AI coding tool.
- **`.copilot`**: GitHub Copilot cached data and configuration.
- **`.boltai`**: BoltAI configurations (an AI app/tool).
- **`.antigravity`, `.antigravity_cockpit`**: Configurations and bins for the Antigravity AI agent framework.
- **`.gemini`**: Used to store context, artifacts, and logs for the Antigravity/Gemini agentic system.
- **`.eclipse`**: Legacy folder for Eclipse IDE settings and workspace metadata.
- **`.chelper`**: Likely a helper tool for competitive programming or C/C++ development.

## 2. Package Managers & Runtimes
These folders store global packages, cached binaries, and environment managers for various programming languages.
- **`.npm`, `.npm-global`**: Node.js package manager cache and global installations.
- **`.nvm`**: Node Version Manager. Stores different installed Node.js versions.
- **`.bun`**: Configuration and global installations for the Bun JavaScript runtime.
- **`.cargo`, `.rustup`**: Rust package manager (Cargo) cache, bins, and Rustup toolchain installations.
- **`.conda`**: Conda environment manager configurations (Python/Data Science).

## 3. Version Control & DevOps Tools
These folders are used by Git, cloud CLIs, and deployment tools.
- **`.github`**: Often stores GitHub Copilot auth or global GitHub workflows.
- **`.docker`**: Docker CLI configurations and authentication contexts.
- **`.aws`, `.azure`**: Configurations and credentials for Amazon Web Services and Microsoft Azure CLIs.
- **`.fly`, `.railway`, `.render`, `.swa`**: CLI configuration and auth tokens for deployment platforms (Fly.io, Railway, Render, Azure Static Web Apps).
- **`.expo`**: React Native Expo CLI cache and configurations.
- **`.ssh`**: Critical folder storing your SSH keys (e.g., `id_rsa`, `id_ed25519`) and `known_hosts` for secure connections.

## 4. Custom Open Universe / Claw Agents
These appear to be custom, specialized AI agents or frameworks unique to your workflow (likely related to your "Open-Universe" and "Multi-Agents" projects).
- **`.openclaw`, `.openclaw-dev`**: OpenClaw agent configurations and completions.
- **`.picoclaw`, `.zeroclaw`, `.clawsec`, `.clawdbot`**: Various specialized "Claw" agents for specific tasks (security, minimal tasks, zero-shot, db tasks).
- **`.mcp-auth`**: Model Context Protocol authentication storage.
- **`.cagent`, `.agents`, `.nanobot`, `.applypilot`, `.haystack`**: Other multi-agent system configs, state, and specialized bots.

## 5. System, OS, and Shell History
These are standard Unix/macOS dotfolders for shell history and system operations.
- **`.Trash`**: macOS user trash bin containing deleted files.
- **`.cache`**: General purpose cache directory used by many Linux/Unix tools natively.
- **`.config`**: Standard XDG config directory (Unix standard) where modern CLI tools store settings (e.g., `gh`, `yarn`).
- **`.local`**: Standard Unix directory (often `~/.local/share` or `~/.local/bin`) for user-specific binaries and isolated app data.
- **`.zsh_sessions`**: Saved states for zsh sessions allowing restoration of terminal history.

## 6. Miscellaneous
- **`.qwen`, `.kimi`**: Configuration and cache for specific LLM providers (Qwen from Alibaba, Kimi by Moonshot AI).
- **`.storybook`**: Global Storybook configurations.
- **`.python-practice`, `.unbrowse`, `.vibe`**: Likely project-specific or tool-specific folders created during standard development.
