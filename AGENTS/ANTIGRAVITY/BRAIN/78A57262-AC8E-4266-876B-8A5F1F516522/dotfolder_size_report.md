# Dotfolder Size & Deletion Analysis

Based on the size scan of your remaining `~/.` folders, here is my analysis of what is consuming space and what you can safely delete.

## 🔴 Largest Space Consumers (Can be reviewed/cleared)

These folders take up the most space. You shouldn't blindly delete the entire folder, but you can safely clear their internal caches if you need space.

1. **`.rustup` (3.9 GB)** & **`.cargo` (1.3 GB)**
   * **What it is:** Rust compiler toolchains and downloaded package/crate registries.
   * **Verdict:** **KEEP**. If you want to free up space, run `cargo cache -a` or `cargo clean` in your Rust projects instead of deleting these folders.
2. **`.vscode` (2.5 GB)** & **`.cursor` (1.5 GB)**
   * **What it is:** Extensions and cached data for VS Code and Cursor.
   * **Verdict:** **KEEP**. If you delete these, you will lose all your IDE extensions and settings.
3. **`.cache` (1.7 GB)**
   * **What it is:** Generic cache directory for many Linux/macOS tools (e.g., pip, yarn, etc.).
   * **Verdict:** **SAFE TO CLEAR**. You can safely delete the contents of `~/.cache/*` to free up 1.7 GB. Programs will just redownload caches as needed.
4. **`.npm` (1.2 GB)**
   * **What it is:** Node.js package manager cache.
   * **Verdict:** **SAFE TO CLEAR**. Do not delete the folder manually; instead, run `npm cache clean --force` in your terminal.

## 🟡 AI & Agent Workspaces (Safe to delete if unused)

These folders belong to various AI agents and CLI tools. If you no longer use the tool, you can safely wipe the folder.

1. **`.cline` (1.3 GB)**
   * **What it is:** Cline (VS Code AI assistant) local data/models.
   * **Verdict:** **Delete if you don't use Cline anymore.**
2. **`.bun` (177 MB)**
   * **What it is:** Bun JavaScript runtime global modules and cache.
   * **Verdict:** Keep if you use Bun.
3. **`.agents` (140 MB)**, **`.openclaw-dev` (70 MB)**, **`.swa` (70 MB)**, **`.copilot` (32 MB)**, **`.zeroclaw` (15 MB)**
   * **What it is:** Custom agent logic, GitHub Copilot caches, and OpenClaw models/data.
   * **Verdict:** **SAFE TO DELETE** if you are no longer actively developing or using these specific agent frameworks.

## 🟢 System, Cloud, and Tiny Configs (DO NOT DELETE)

These folders are either critical for system operation, hold authentication tokens, or are too small to care about (under 10 MB).

* **`.ssh` (4.0 KB):** **NEVER DELETE.** Contains your secure connection keys.
* **`.aws`, `.azure`, `.fly`, `.render`, `.railway` (Under 1 MB combined):** **DO NOT DELETE.** These hold your cloud login credentials and tokens. If you delete them, you will have to log in to all your cloud providers again.
* **`.gitconfig` (4.0 KB), `.npmrc` (4.0 KB), `.zshrc` (4.0 KB), `.zshenv`, etc.:** **NEVER DELETE.** Critical configuration files for Git, Node, and your Terminal.
* **`.config`, `.local`:** Standard Unix directories. Do not delete them blindly.
* **Various others like `.claude`, `.kimi`, `.qwen`, etc.:** Just plain text configuration files taking up less than 1 MB. Completely harmless to keep.

---

### Recommended Action Plan for Maximum Cleanup:

If you want to quickly free up ~3-4 GB of space without breaking your development environment, run these commands in your terminal:

```bash
# Safely clear NodeJS package cache (frees ~1.2 GB)
npm cache clean --force

# Safely clear generic utility caches (frees ~1.7 GB)
rm -rf ~/.cache/*

# (Optional) Delete AI agent workspaces if you no longer use them:
rm -rf ~/.cline ~/.agents ~/.openclaw-dev ~/.zeroclaw
```
