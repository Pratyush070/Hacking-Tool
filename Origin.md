# ORIGIN & CHANGES

**Repository:** Pratyush070 / `Hacking-Tool`  
**Owner:** Pratyush (GitHub: @Pratyush070)  
**Purpose of this file:** Clearly state what in this repository is original work by the owner and what was used as inspiration or forked from public projects. This is written to be transparent for recruiters, maintainers and auditors.

---

## Original inspiration / upstream
This project was initially created as a learning/forked reference from publicly available "all-in-one" security tool repositories. The main public project(s) that served as reference include (but may not be limited to):

- `Z4nzu/hackingtool` (example of a widely-known upstream project) — used only as public reference/inspiration.

If you are the original author of an upstream file referenced here and believe credit is missing, please open an issue or PR.

---

## My (Pratyush) contributions — what I added / changed (explicit)
I have modified and extended the repository to include original code, documentation, tests and an extra resume-impact project. Below is a clear list of what I implemented (these changes are present in the repository history and files listed below):

### Code & architecture changes
- **Rewrote the core CLI** — replaced the original monolithic script with a modular command-line interface implemented in `core.py` and `toolkit/cli.py`. The CLI uses subcommands and a configuration file (`config.yml`) to enable safer, clearer usage.
  - Files: `core.py`, `toolkit/cli.py`, `config.yml`
  - Commit example: `feat(cli): modularize CLI and add config-driven commands` — (replace with actual commit hash)

- **Modularized the codebase** — separated functionality into a small package structure (`toolkit/`), splitting responsibilities (core logic, utils, installers).
  - Files/folders: `toolkit/`, `toolkit/core.py`, `toolkit/utils.py`

- **Removed bundled zip and cleaned repo** — removed `hackingtool-master.zip` and other bulk uploads to avoid verbatim copies and to keep the repo source-controlled.
  - File removed: `hackingtool-master.zip`
  - Commit example: `chore: remove bundled zip file`

- **Packaging & install improvements** — added `setup.py` / `pyproject.toml` and a simple `install.sh` that uses proper dependency installation (no large bundled binaries).
  - Files: `setup.py`, `requirements.txt`, `install.sh`

### New features (original)
- **Auto-update check** — small feature that checks for updates from asafe source and notifies the user (implemented as `toolkit/updater.py`).
- **Auth-proxy stub** — an opt-in stub that demonstrates how sensitive operations would require authenticated approval (implemented as `toolkit/auth_proxy.py`).
- **Logging & safety modes** — added structured logging (`logging.config`) and an explicit `--safe-mode` flag that disables risky commands by default.

### Tests & CI
- **Unit tests** — added simple unit tests to verify core logic and parsing (`tests/test_core.py`, `tests/test_utils.py`).
- **GitHub Actions** — added a CI workflow `.github/workflows/python-app.yml` to run tests on push/PR.

### Documentation & artifacts
- **ORIGIN.md** (this file) — transparent origin & changes.
- **README.md** — rewritten to describe current scope, usage, and limitations; includes a clear "What I wrote" section and a "What is upstream" section.
- **CHANGELOG.md** — short changelog summarizing my edits and versions.
- **docs/** — added usage screenshots and a short demo GIF (`docs/screenshots/`, `docs/demo.gif`).

### Additional original project (resume-impact)
- **`projects/job-resume-matcher/`** — a small, original NLP project I implemented and added to this repository to demonstrate applied ML/NLP skills:
  - Tech: Python, Flask, TF-IDF + sentence-transformers
  - Functionality: upload JD + resume (text/PDF) → returns a 0–100 match score, highlights missing keywords, and suggests 5 resume improvement bullets.
  - Files: `projects/job-resume-matcher/app.py`, `projects/job-resume-matcher/matcher/`, `projects/job-resume-matcher/README.md`, `projects/job-resume-matcher/Dockerfile`
  - This project is fully implemented by me and is not copied from another repository.

---

## License & attribution
- This repository is released under the **MIT License** (or the license declared in `LICENSE`).  
- Where code, examples or ideas are derived from other public projects under permissive licenses (MIT/Apache/BSD), I include explicit attribution in the relevant files and/or in `ORIGIN.md` (see "Original inspiration" above).  
- If any upstream author requests additional credit or changes, I will promptly update the attribution.

---

## For recruiters / maintainers — quick verifiable pointers
If a recruiter or maintainer wants to verify contributions quickly, please check the following:
- Example commit showing core changes: `git show <commit-hash-core>` — (replace with the actual commit hash for the CLI rewrite)
- Tests added: `tests/test_core.py` and CI run results: check Actions tab
- New project: `projects/job-resume-matcher/` — contains full README, run instructions and Dockerfile

If you need a quick walkthrough, I can live-demo specific commits and explain the code I wrote line-by-line.

---

## Contact / Author
**Pratyush** — GitHub: [@Pratyush070](https://github.com/Pratyush070)  
Email: pratyushpathak695@gmail.com

---

*Note:* This file is intended to be honest and transparent. If you want me to replace placeholders with actual commit hashes/dates/links, tell me and I will generate the exact `git` commands to extract them (so you can paste accurate references).
