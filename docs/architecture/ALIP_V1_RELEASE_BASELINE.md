# ALIP v1.0 — QMS_TAT RELEASE BASELINE

## Release

**Version:** ALIP v1.0  
**System:** QMS_TAT  
**Status:** Release Baseline Verified

## Verified Architecture

- Domain layer
- Application layer
- Infrastructure layer
- Persistence boundary
- Interface/API layer
- FastAPI integration
- End-to-end TAT workflow
- Observability layer
- Health endpoint

## Quality Gates

- Ruff auto-fix
- Ruff verification
- Ruff format
- Black
- Isort
- Mypy
- Bandit
- Pytest
- Coverage >= 90%

## Release Principle

The v1.0 baseline is frozen only when:

1. All quality gates pass.
2. Full regression passes.
3. Working tree is clean.
4. Local `main` matches `origin/main`.
5. No uncommitted implementation remains.

## Next Development Track

Post-v1.0 work must begin from a new build identifier and must not
silently modify the frozen v1.0 baseline.
