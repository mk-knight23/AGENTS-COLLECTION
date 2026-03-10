# Global Antigravity Configuration

This file defines the global capabilities and resources available across all projects for the Antigravity agent.

## 🛠️ Global Skills

The following specialized skills are available globally and should be prioritized for their respective tasks:

- **git-commit-formatter**: Use this for all Git commits to ensure Conventional Commits compliance.
- **license-header-adder**: Use this when creating new source files that require an Apache 2.0 copyright header.
- **json-to-pydantic**: Use this to convert JSON data snippets into Python Pydantic models.
- **database-schema-validator**: Use this to validate SQL schema files against safety and naming policies.
- **adk-tool-scaffold**: Use this to scaffold new Tool classes for the Agent Development Kit (ADK).

## 🚀 Global Workflows (Slash Commands)

The full Antigravity Kit is available globally. You can use these commands to streamline your work:
- `/brainstorm`: Structured idea exploration.
- `/create`: New application generation.
- `/debug`: Systematic problem investigation.
- `/deploy`: Production deployment and pre-flights.
- `/enhance`: Iterative feature development.
- `/orchestrate`: Multi-agent coordination.
- `/plan`: Project planning and task breakdown.
- `/preview`: Development server management.
- `/status`: Project and agent status overview.
- `/test`: Test generation and execution.
- `/ui-ux-pro-max`: AI-powered design system generation.

## ⚖️ Global Guidelines

- **Proactivity**: Always suggest using these global tools if they are relevant to the user request.
- **Consistency**: Follow the global rules defined in `~/.gemini/antigravity/rules/`.
