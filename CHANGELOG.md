# Changelog

All notable changes to geocardo will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Repository scaffolding: monorepo layout with Cargo workspace and Python package
- PyO3 entry point (`geocardo._native`) with sanity `_version()` function
- Project metadata: README, CONTRIBUTING, CHANGELOG, LICENSE (MIT)
- Build configuration: pyproject.toml (maturin + uv dependency-groups), Cargo.toml workspace, ruff, ty, pytest
- uv-based development workflow (`uv sync`, `uv run`) with CI via `astral-sh/setup-uv`
- Initial sanity tests
