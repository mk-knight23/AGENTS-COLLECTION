# Advanced Intelligent System Discovery Plan

## Goal Description
The objective is to intelligently reverse-engineer and reconstruct knowledge systems for 5 AI toolsets (AI-CLAUDE-CODE, AI-ANTIGRAVITY, AI-CODEX, AI-OPENCODE, AI-CURSOR). Instead of merely copying files, the system will read terminal histories (`.zsh_history`, `.bash_history`), analyze scripts, and synthetically infer workflows, productivity skills, agent architectures, and prompt libraries.

## Proposed Changes

### 1. Terminal History Analysis
- We will parse `~/.zsh_history` and `~/.bash_history`.
- Extract command sequences invoking `claude`, `cursor`, `claw`, `nanobot`, `mcp`, etc.
- Identify patterns such as loops, deployment pipelines, and prompt flows.

### 2. Deep Artifact Extraction
Using the previous system scan as a baseline, a new Python analysis script will be run to semantically dissect:
- **Prompts**: Extract `<Prompt>` tags, markdown blockquotes, or variables named `prompt`.
- **Workflows**: Map out sequences from bash/python auto-scripts.
- **Agent Architectures**: Discover MCP server configs, multi-agent LLM routers, and tool definitions.

### 3. Repository Knowledge Synthesis
Each of the 5 repositories in `/tmp/AI_TOOL_RECONSTRUCTION_V2/` will generate the following advanced structure:
- `/docs/skills.md`, `/docs/workflows.md`, `/docs/prompts.md`, `/docs/automation.md`, `/docs/integrations.md`, `/docs/architecture.md`
- `/scripts/automation`, `/scripts/tools`, `/scripts/examples`
- `/patterns/agent-patterns.md`, `/patterns/prompt-patterns.md`, `/patterns/code-generation.md`
- `/config/tool-configs`
- `/research/discoveries.md`, `/research/workflow-analysis.md`

The Python script will synthesize content for "Skills" based on whether advanced scripting features (e.g. MCP integration) or multi-agent routing were found.

### 4. Delivery
Due to the macOS SIP, the final result will be zipped to `/tmp/AI_TOOL_RECONSTRUCTION_V2.zip` with a command provided to extract it to `~/`.

## Verification Plan
1. Ensure the new repo structure perfectly matches the Phase 9 instructions.
2. Verify that `zsh_history` was successfully parsed and commands synthesized into workflows.
3. Validate that no duplicate, binary, or build payload folders were included.
