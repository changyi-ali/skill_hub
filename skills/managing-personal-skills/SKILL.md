---
name: managing-personal-skills
description: Use when creating, updating, renaming, or removing a user-authored personal Codex Skill that must be archived in the skill_hub Git repository and pushed to its configured remote.
---

# Managing Personal Skills

Keep the installed Skill and its Git archive synchronized. The runtime copy remains under `/Users/richard/.codex/skills/<skill-name>`; the reviewed archive lives under `/Users/richard/code/skill_hub/skills/<skill-name>`.

## Scope

Archive only Skills Richard created or explicitly took ownership of. Exclude `.system`, plugin/cache content, vendor Skills, and any Skill with an external-source marker such as `x-source: aone-open`. If ownership is unclear, ask before copying.

## Required workflow

1. Finish the Skill change in its runtime directory. For new or substantially revised Skills, use `skill-creator` and `superpowers:writing-skills`.
2. Run the official validator through Python:

   ```bash
   python3 /Users/richard/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
     /Users/richard/.codex/skills/<skill-name>
   ```

3. Verify that the frontmatter `name` equals the source-directory basename and that the target resolves exactly to `/Users/richard/code/skill_hub/skills/<skill-name>`.
4. Mirror the complete runtime directory into that target. For an existing archive, propagate additions, changes, and removals only inside the exact target Skill directory; Git is the recovery boundary.
5. Require a clean recursive comparison:

   ```bash
   diff -qr /Users/richard/.codex/skills/<skill-name> \
     /Users/richard/code/skill_hub/skills/<skill-name>
   ```

6. Inspect the archive for credentials, private keys, tokens, unfinished scaffold placeholders, and accidental generated files. Run `git diff --check` and review the full diff.
7. Preserve unrelated work. Stage only the exact Skill path plus intentionally updated archive documentation. If unrelated edits overlap those paths, stop and ask the user.
8. Commit with a message that distinguishes creation from synchronization, then push the current branch to its configured upstream. This user has explicitly requested pushes for personal-Skill archival work.
9. Fetch or inspect the tracking ref and verify that local `HEAD` equals its upstream. Report the commit ID and archived path.

## Repository inventory

When adding, renaming, or removing a Skill, update `/Users/richard/code/skill_hub/README.md`. Never remove the runtime copy merely because the archive was updated.

## Completion contract

Do not claim archival is complete unless validation passes, runtime and archive trees match, the scoped commit succeeds, and the remote tracking ref contains the same commit.
