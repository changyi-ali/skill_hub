---
name: visualizing-code-summaries
description: Use when the user explicitly asks for an image, diagram, 彩图, architecture diagram, or visual explanation to summarize code architecture, explain code features, or present commit or change history.
---

# Visualizing Code Summaries

Turn verified code evidence into a concise, colorful, standalone HTML explanation. Do not trigger for an ordinary text-only code summary, generic data chart, product mockup, photograph, or illustration.

**REQUIRED SUB-SKILL:** Use `visualize:visualize` for HTML composition, accessibility, theme variables, responsive behavior, rendering, and visual inspection.

## Evidence first

Inspect the requested source code, module documentation, tests, Git log, and commit diff before drawing. Every component, edge, state transition, ownership label, and example value must be supported by those materials. Mark useful but unverified conclusions as `推断` or `待确认`; never invent missing structure to make the picture look complete.

## Choose one primary mode

- **Architecture:** layers or lanes, process/repository boundaries, dependency direction, entry points, data flow, and system constraints.
- **Feature:** numbered phases with actors, inputs, actions, decisions, state changes, errors, and results.
- **Commit changes:** before/after comparison, responsibility moved across repositories or modules, additions/removals, compatibility impact, and user-visible behavior.

For a mixed request, select one primary mode and use the others only as supporting regions. Read [references/visual-style.md](references/visual-style.md) before composing the visual.

## Output contract

1. Create a concise ASCII lowercase-hyphenated filename.
2. Always deliver a complete standalone `.html` document under `/Users/richard/code/picture`; never stop at an in-conversation fragment. Do not silently fall back to another directory if access is unavailable.
3. Use the `visualize:visualize` fragment workflow as the editable source, then render/export it to the standalone destination. Remove or replace host-only interactions such as `window.openai` before export.
4. Avoid overwriting an existing file unless the user explicitly requests replacement; add a meaningful suffix when needed.
5. Inspect the rendered result at desktop width and a narrow width near 320px. Fix overlaps, clipping, unreadable contrast, broken arrows, missing labels, and runtime errors.
6. In the final response, link the absolute HTML path and state at most one key conclusion. Do not repeat the diagram as a long textual summary.

## Quality bar

Prefer one dominant flow, stable semantic colors, explicit arrows, real code symbols, and short labels. Keep facts distinguishable from inference and pair color with text or shape. If the explanation remains too dense after removing secondary detail, split it into multiple standalone HTML files rather than shrinking text.
