# Personal Skill Archive Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish `skill_hub` as the Git archive for Richard's personal Codex skills, then create and archive the first new visualization skill.

**Architecture:** Runtime copies remain under `~/.codex/skills`; the repository stores reviewed mirrors under `skills/`. A management skill makes validation, mirroring, scoped commits, and pushes part of every future personal-skill create/update workflow. The visualization skill builds evidence-backed standalone HTML summaries in `/Users/richard/code/picture`.

**Tech Stack:** Markdown Agent Skills, YAML metadata, Git, shell-based validation, Codex `visualize:visualize` export workflow.

**Spec:** `/Users/richard/code/picture/2026-09-17-code-visual-summary-skill-design.md` plus the approved `skill_hub` archive design in this task.

## Global Constraints

- Do not move or delete runtime skills from `/Users/richard/.codex/skills`.
- Archive only user-authored personal skills; exclude system, plugin, cached, and externally sourced skills such as `x-source: aone-open`.
- Store archived skill trees under `/Users/richard/code/skill_hub/skills/<skill-name>`.
- Validate every new or changed skill before commit.
- Commit only files belonging to this archive change and push the resulting commit to `origin`.
- Every code visualization is a standalone `.html` file under `/Users/richard/code/picture`.

---

### Task 1: Archive repository policy and baseline skills

**Files:**
- Modify: `/Users/richard/code/skill_hub/README.md`
- Create: `/Users/richard/code/skill_hub/AGENTS.md`
- Archive: `/Users/richard/code/skill_hub/skills/dash-dev-server-remote/**`
- Archive: `/Users/richard/code/skill_hub/skills/kvs-fast-check/**`

**Interfaces:**
- Consumes: runtime skills under `/Users/richard/.codex/skills`.
- Produces: repository layout and rules used by future personal-skill work.

- [ ] **Step 1: Record a failing baseline**

Run checks proving that `skills/dash-dev-server-remote`, `skills/kvs-fast-check`, and the archive policy do not yet exist.

- [ ] **Step 2: Add repository policy and inventory**

Document the runtime/archive split, exclusion rules, validation, scoped commit, and push workflow in `README.md` and `AGENTS.md`.

- [ ] **Step 3: Mirror existing personal skills**

Copy the complete two skill directories into `skills/` without modifying their runtime copies.

- [ ] **Step 4: Verify mirror integrity**

Use recursive diffs and skill validation to prove archive copies match their runtime sources.

### Task 2: Personal-skill archive management skill

**Files:**
- Create: `/Users/richard/.codex/skills/managing-personal-skills/SKILL.md`
- Create: `/Users/richard/.codex/skills/managing-personal-skills/agents/openai.yaml`
- Archive: `/Users/richard/code/skill_hub/skills/managing-personal-skills/**`

**Interfaces:**
- Consumes: a user-authored skill directory under `/Users/richard/.codex/skills/<name>`.
- Produces: a validated mirror under `skill_hub/skills/<name>`, one scoped Git commit, and a push to the configured upstream.

- [ ] **Step 1: Write contract checks before the skill exists**

Check that the skill is absent and define assertions for trigger scope, external-source exclusion, validation, mirror comparison, scoped commit, and push.

- [ ] **Step 2: Create the minimal management skill**

Write a concise workflow that triggers for creation, update, rename, or removal of user-authored personal skills and explicitly excludes third-party/system skills.

- [ ] **Step 3: Validate and archive the management skill**

Run `quick_validate.py`, run contract checks, copy the complete directory into `skill_hub/skills`, and prove the trees match.

### Task 3: Standalone code-summary visualization skill

**Files:**
- Create: `/Users/richard/.codex/skills/visualizing-code-summaries/SKILL.md`
- Create: `/Users/richard/.codex/skills/visualizing-code-summaries/agents/openai.yaml`
- Create: `/Users/richard/.codex/skills/visualizing-code-summaries/references/visual-style.md`
- Archive: `/Users/richard/code/skill_hub/skills/visualizing-code-summaries/**`

**Interfaces:**
- Consumes: source code, module documents, Git history/diffs, and an explicit user request for visual explanation.
- Produces: one evidence-backed standalone HTML file under `/Users/richard/code/picture`.

- [ ] **Step 1: Write contract checks before the skill exists**

Define assertions for explicit visual triggering, architecture/feature/commit modes, evidence versus inference, required standalone output directory, responsive/theme-aware style, and the `visualize:visualize` dependency.

- [ ] **Step 2: Create the minimal skill and style reference**

Keep routing and output invariants in `SKILL.md`; place detailed layout recipes and the reusable visual language in `references/visual-style.md`.

- [ ] **Step 3: Validate and archive the visualization skill**

Run `quick_validate.py`, contract checks, copy the complete directory into `skill_hub/skills`, and prove the trees match.

### Task 4: Repository verification, commit, and push

**Files:**
- Verify all changed files under `/Users/richard/code/skill_hub`.

**Interfaces:**
- Consumes: verified archive contents from Tasks 1–3.
- Produces: a clean local `main` synchronized with `origin/main`.

- [ ] **Step 1: Run complete validation**

Validate every archived skill, compare every runtime/archive pair, inspect for secrets and unfinished placeholders, and review `git diff --check` plus `git diff`.

- [ ] **Step 2: Commit only archive files**

Stage the exact policy, plan, and skill paths; create one commit describing the personal skill archive and visualization skill.

- [ ] **Step 3: Push and verify remote state**

Push the current branch to its configured upstream, then verify local HEAD equals `origin/main` and the worktree is clean.
