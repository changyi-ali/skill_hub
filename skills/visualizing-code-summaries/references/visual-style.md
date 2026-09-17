# Visual Style Reference

Read this reference only when producing a code-summary visual.

## Visual signature

Use the visual language established by `kvcm-tair-mempool-deferred-bootstrap-flow.html` without copying its business content:

- concise title and one-line subtitle;
- a compact legend when color identifies repositories, components, phases, or states;
- numbered phase cards connected by unmistakable arrows;
- low-opacity semantic color fills rather than heavily colored borders;
- real function, flag, field, module, or commit names in `<code>`;
- compact tables for selection rules or direct comparisons;
- one restrained result, compatibility, or removed-complexity strip when it changes the reader's conclusion.

Use a transparent, unframed top-level surface. Cards represent bounded phases or states, not every structural grouping. Avoid dashboard-like KPI tiles, ornamental gradients, oversized icons, invented status badges, and repeated legends.

## Layout recipes

### Architecture

Arrange components as layers or swimlanes. Show control flow and data flow with different labels or line treatments when both matter. Identify cross-process, cross-repository, network, or persistence boundaries explicitly. Put system-wide invariants near the affected boundary rather than in a detached notes panel.

### Feature

Use three to five numbered stages when the lifecycle is central. Each stage answers: who acts, what enters, what happens, what state changes, and what leaves. Put a decision table or ordered rule inside the stage that owns the decision. Show important failure paths, but omit routine implementation detail.

### Commit changes

Lead with a compact `before → change → after` comparison. Follow with repository or module ownership only when changes span boundaries. Distinguish added, moved, replaced, and removed responsibilities through labels as well as color. Include commit IDs only when they help trace evidence.

## Color and typography

- Use only theme-aware variables supplied by `visualize:visualize`, including `--foreground`, `--muted-foreground`, `--border`, `--card`, `--primary`, `--destructive`, `--green`, `--orange`, `--purple`, and `--viz-series-1` through `--viz-series-6`.
- Assign a color to a persistent semantic identity, not to decoration. Use the same mapping everywhere in the document.
- Pair every color distinction with visible text, position, icon, or shape.
- Use normal body text and reserve `.text-small` for secondary annotations. Never reduce visible text below 11 screen pixels.
- Keep code strings wrappable with `overflow-wrap:anywhere`; do not truncate identifiers that explain the flow.

## Responsive and accessible behavior

Design first for approximately 736px. At widths below the card grid's readable minimum, stack phases vertically and rotate or replace horizontal arrows so direction remains obvious. Support 320px without horizontal page scrolling, clipped tables, or overlapping labels.

Use semantic sections, headings, tables, and lists. Give the main diagram a concise accessible label. Mark decorative arrows and icons `aria-hidden="true"`. Essential information must remain available without hover, and color contrast must remain readable in both light and dark themes.

## Evidence labels

Facts appear without qualification only when source material supports them. Prefix uncertain content visibly with `推断：` or `待确认：`. Do not mix inferred arrows into a factual call chain without that label.

## Final inspection

Before export, check that:

- the visual answers the user's question without accompanying prose;
- arrow direction matches the real call or data flow;
- repository and component ownership is consistent;
- examples are real or explicitly labeled illustrative;
- the first viewport exposes the dominant story;
- desktop and narrow layouts remain readable;
- no KVCM-, TairMempool-, or other project-specific content is hard-coded into the reusable Skill.
