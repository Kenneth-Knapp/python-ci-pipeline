\# Python CI Pipeline (Demo)



!\[CI](https://github.com/Kenneth-Knapp/python-ci-pipeline/actions/workflows/ci.yml/badge.svg)



\*\*Purpose:\*\* Demonstrate SDLC discipline with automated formatting, linting, type checks, security scan, and unit tests via GitHub Actions.



\*\*Stack:\*\* Python 3.13, pytest, black, flake8, mypy, bandit, GitHub Actions.





\## Local Development



```bash

python -m venv .venv



\# Windows:

.venv\\Scripts\\activate



\# macOS/Linux:

\# source .venv/bin/activate



pip install -r requirements-dev.txt

pytest -q --maxfail=1 --disable-warnings

black --check .

flake8 .

mypy src --ignore-missing-imports

bandit -q -r src





\## CI Details

On every push and pull request, GitHub Actions runs:

\- \*\*Black\*\* (format check)

\- \*\*Flake8\*\* (lint)

\- \*\*Mypy\*\* (static typing)

\- \*\*Bandit\*\* (security scan)

\- \*\*Pytest\*\* with coverage (artifact: `coverage.xml`)



\## Project Layout

src/            # application code

tests/          # unit tests (pytest)

.github/        # CI workflows and repo settings





\## Contributing

\- Create a feature branch: `git checkout -b feature/<name>`

\- Commit with clear messages (e.g., `feat: add X`)

\- Open a Pull Request to `main` (CI must pass)







