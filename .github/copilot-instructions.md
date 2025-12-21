# Copilot instructions — Generative_AI_With_Python_At_DEVELOPERS.INSTITUTE

Purpose
- Help AI agents make focused, low-risk edits in this educational exercises repository.

Big picture
- This repo is a set of small, standalone Python exercise scripts organized by week/day under `Week1/Day1`, `Week1/Day2`, `Week1/Day4`, etc.
- There is no package structure, CI, or dependency manifest; files are intended to be runnable scripts for learning.
- Primary intent: keep exercises runnable and minimal; avoid broad refactors that change exercise intent.

Key files (examples)
- [Week1/Day4/Week1Day4Exercises.py](Week1/Day4/Week1Day4Exercises.py) — representative exercises file. Treat similar files in `Week1/**` the same way.
- [Week1/Day2/Week1Day2Exercises.py](Week1/Day2/Week1Day2Exercises.py)
- [Week1/Day1/personalpractice.py](Week1/Day1/personalpractice.py)

Conventions & patterns (discoverable)
- Each file contains short, independent exercises implemented as plain Python scripts, often with interactive `input()` lines and commented blocks.
- Many lines are commented out (solutions or notes). Preserve original commented content unless instructed to fully replace it.
- Filenames follow `Week{N}/Day{M}/*Exercises.py`. When adding new exercises, follow this path convention.

Developer workflows (how to run and test locally)
- No virtualenv or requirements file present. Use system Python.
- Run an exercise directly from the repo root. Example (Windows PowerShell):

```powershell
python Week1/Day4/Week1Day4Exercises.py
```

- Alternatively run as module if you add __init__ files (not currently used):

```bash
python -m Week1.Day4.Week1Day4Exercises
```

Editing guidance for AI agents
- Small, focused edits only: update one exercise file per change/PR and keep changes minimal.
- When modifying interactive code (`input()`), ensure the script still runs non-exceptional flows (validate with quick local run).
- Do not introduce new external dependencies. If a dependency is required, explicitly ask the user first.
- Preserve educational intent: avoid rewriting exercises into large libraries or radically changing the user-facing outputs.

Patterns to follow in examples
- If adding a helper, add it inside the same file or a new util under `Week1/utils.py` and document usage in that file.
- Keep prints and prompts clear and user-friendly; these are student-facing scripts.

Debugging notes
- Use quick `print()` statements and run the script in PowerShell/terminal to reproduce issues.
- There are no tests; validate by running the modified file(s).

Commit & PR guidance
- Use concise commit messages and keep PRs limited to one week/day folder where possible.
- If changes affect multiple days/weeks, explain the rationale in the PR description and request review from the repo owner.

Do / Don't summary
- Do: Keep changes minimal, run scripts locally, reference example files above when unsure.
- Don't: Add packages without approval, perform large-scale refactors, remove original commented exercises without confirming.

If anything is unclear or you want additional conventions (e.g., preferred formatting, test harness), tell me which files or patterns to inspect and I will expand this file.