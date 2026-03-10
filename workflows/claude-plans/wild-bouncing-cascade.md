# Plan: Unified AI Provider Strategy

## Context

The goal is to unify the AI provider configuration across four projects: `openclaw`, `nanoclaw`, `picoclaw`, and `zeroclaw`. Currently, each project has a disparate, difficult-to-maintain configuration. This plan will create a centralized, benchmark-driven strategy to improve reliability, performance, and cost-effectiveness across the entire ecosystem.

## Implementation Plan

### Phase 1: Benchmark All Providers

1.  **Create Benchmarking Tool**: Develop a new CLI command, `openclaw models benchmark`, within the `openclaw` project. This tool will automate the testing of all 80+ models across the 20 configured providers.
2.  **Define Test Suite**: Create a standardized test suite (in YAML) to evaluate models on key capabilities:
    *   Simple Q&A (speed and correctness)
    *   Code Generation (logic and syntax)
    *   Reasoning & Logic (complex problem-solving)
    *   Summarization (comprehension)
3.  **Capture Metrics**: The benchmark will capture the following for each model:
    *   **Latency**: Time to first token and total response time.
    *   **Success Rate**: Percentage of successful API calls.
    *   **Cost**: Estimated cost per 1M tokens (input/output), using `zeroclaw`'s pricing data as a baseline.
    *   **Quality**: Automated and manual scores based on test suite performance.
4.  **Generate Report**: The tool will output a structured report (JSON or CSV) for analysis.

### Phase 2: Design and Implement Unified Configuration

1.  **Create a Tiered Model Catalog**: Based on benchmark results, create a single `models.json` file that all projects will share. Models will be organized into four tiers:
    *   **Tier 1 (Free/Low-Cost)**: Top-performing free models for high-volume tasks.
    *   **Tier 2 (Primary Performers)**: The best all-around models (default for most operations).
    *   **Tier 3 (Specialist Models)**: Models excelling at specific tasks (e.g., `codestral-latest` for code).
    *   **Tier 4 (Premium)**: Most powerful/expensive models for critical tasks (e.g., `glm-5`).
2.  **Define Intelligent Fallback Chain**: Using `zeroclaw`'s `config.toml` as a template, define a robust, multi-layered fallback chain in the central configuration.
3.  **Centralize Key Management**: Consolidate all API keys into a single, secure `auth-profiles.json` and reference them from the main configuration. The system will support multiple keys per provider with automatic rotation.

### Phase 3: Refactor All Projects to Use Unified Config

1.  **Refactor `openclaw`**: Update its core logic (`models-config.ts`, `model-fallback.ts`) to consume the new `models.json` and `auth-profiles.json`.
2.  **Refactor `nanoclaw`**: Replace its hardcoded provider list in `config.json` with a reference to the unified configuration. Set its default model to a cost-effective Tier 2 provider.
3.  **Refactor `picoclaw`**: Remove the redundant `model_list` from its `config.json` and integrate the unified configuration. Set its default to a strong Tier 2 reasoning model to complement its web search functions.
4.  **Refactor `zeroclaw`**: While its principles form the foundation, it will be updated to consume the new `models.json` directly, ensuring consistency while retaining its advanced security and autonomy settings.

### Phase 4: Verification

1.  **Unit & Integration Tests**: Add tests to `openclaw` to verify that the new configuration is loaded correctly and that the fallback logic works as expected.
2.  **End-to-End Validation**: Run the `openclaw models benchmark` command through each project's configuration to confirm that all models are accessible and performant.
3.  **Manual Verification**: Perform a final manual check on each project to ensure its core functionality remains intact after the refactoring.

## Critical Files to Modify

*   `/Users/mkazi/Open-Universe/openclaw/src/agents/models-config.ts`
*   `/Users/mkazi/Open-Universe/openclaw/src/agents/model-fallback.ts`
*   `/Users/mkazi/Open-Universe/openclaw/src/config/types.models.ts`
*   `/Users/mkazi/Open-Universe/openclaw/src/infra/session-cost-usage.ts`
*   `/Users/mkazi/.nanobot/config.json`
*   `/Users/mkazi/.picoclaw/config.json`
*   `/Users/mkazi/.zeroclaw/config.toml`
