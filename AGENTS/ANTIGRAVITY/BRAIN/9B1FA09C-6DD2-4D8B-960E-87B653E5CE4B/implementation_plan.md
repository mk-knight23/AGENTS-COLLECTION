# Implementation Plan - Pipeline Evolution v2.1

Upgrade the pipeline to transform GitHub web repositories into "Real Apps" with automated deployment and precise design mapping.

## Proposed Changes

### Core Models & Infrastructure

#### [MODIFY] [models.py](file:///Users/mkazi/GitLab%20Mobile%20/repo-evolution-pipeline/pipeline/core/models.py)
- Update `DeepAnalysis` to include `extracted_theme`: a dictionary of colors, font names, and UI style hints.
- Update `MobileFramework` enum: Mark `FLUTTER` and `IONIC` as deprecated (to be removed in this phase).
- Add `eas_enabled` flag to `MobileArchitecture`.

---

### Analysis & Design Extraction

#### [MODIFY] [analyzer.py](file:///Users/mkazi/GitLab%20Mobile%20/repo-evolution-pipeline/pipeline/agents/analyzer.py)
- Enhance `analyze_repo_deep` prompt to specifically extract primary/secondary/background hex colors from CSS/Tailwind files.
- Add logic to map detected web UI patterns to mobile-friendly equivalents.

---

### Code Generation & Design System

#### [MODIFY] [tokens.py](file:///Users/mkazi/GitLab%20Mobile%20/repo-evolution-pipeline/pipeline/templates/design_system/tokens.py)
- Refactor `generate_theme_file` to accept an `overrides` dictionary, allowing extracted colors/fonts to replace defaults.

#### [MODIFY] [codegen.py](file:///Users/mkazi/GitLab%20Mobile%20/repo-evolution-pipeline/pipeline/agents/codegen.py)
- **[DELETE]** Remove all Flutter and Ionic generation logic.
- Update `generate_mobile_code` to pass extracted theme tokens to the theme generator.
- Enhance `_llm_generate_screen` prompt to emphasize "Premium Design" and use the extracted tokens.

---

### Deployment & CI/CD

#### [MODIFY] [ci_templates.py](file:///Users/mkazi/GitLab%20Mobile%20/repo-evolution-pipeline/pipeline/agents/ci_templates.py)
- **[NEW]** Add `deploy_eas` job to the `expo` template.
- Implement EAS (Expo Application Services) build and update triggers.
- Remove Flutter and Ionic CI templates.

---

## Verification Plan

### Automated Tests
- Run `python -m pipeline health` to verify core integrity.
- Execute unit tests for the new token mapping logic.

### Manual Verification
1. Target a real GitHub web repo (e.g., a simple landing page or dashboard).
2. Run `python -m pipeline run-single --repo "user/repo"`.
3. Verify that the generated `src/theme/index.ts` contains colors matching the original web repo.
4. Check that the GitLab CI pipeline includes the new `deploy` stage.
