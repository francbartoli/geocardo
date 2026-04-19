# Contributing to geocardo

## Development setup

You need:

- [uv](https://docs.astral.sh/uv/) — Python package manager (install: `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- [rustup](https://rustup.rs/) — Rust toolchain

uv handles Python itself, the virtual environment, dependencies, and the Rust extension rebuild. You don't need to install Python separately.

```bash
git clone https://github.com/francbartoli/geocardo.git
cd geocardo

# Install Python, create .venv, install all deps (including dev group) and
# build the Rust extension in editable mode. One command.
uv sync

# Run anything inside the project environment with `uv run`:
uv run pytest
uv run ruff check .
uv run ty check
```

`uv sync` automatically runs `maturin develop` under the hood because maturin is the build backend declared in `pyproject.toml`. Re-run `uv sync` (or `uv sync --reinstall-package geocardo`) after changing Rust code.

## Running tests

```bash
uv run pytest                           # Python tests (includes Rust binding tests)
cargo test --workspace                  # pure Rust tests
```

## Linting and type checking

```bash
uv run ruff check .
uv run ruff format --check .
cargo clippy --workspace -- -D warnings
cargo fmt --all --check
uv run ty check
```

> [!note]
> **ty** is Astral's type checker, part of the same toolchain as ruff and uv. It's in preview (pre-1.0) but actively developed and already covers most real-world Python code. Consistent with the rest of our stack. If you hit a ty limitation, the escape hatch is `# ty: ignore[rule-name]` on the offending line; document why in a comment.

## Lockfile

`uv.lock` is committed. It pins exact versions of all Python dependencies for deterministic builds across machines and CI. Update it with `uv lock --upgrade` (all deps) or `uv lock --upgrade-package <name>`. Similarly, `Cargo.lock` is committed at the workspace root.

## Project structure

```
geocardo/
├── crates/                         # Cargo workspace
│   ├── geocardo-py/                # PyO3 bindings (entry point: _native)
│   ├── geocardo-catalog/           # added in v0.1: OGC OpenAPI -> compiled catalog
│   └── geocardo-geojson/           # added in v0.10: GeoJSON serializer (optional)
├── src/geocardo/                   # Python package
│   ├── domain/                     # DDD: Aggregates, Value Objects, Domain Services
│   ├── application/                # Use cases, application services
│   ├── adapters/                   # Inbound (HTTP, config) and outbound (providers)
│   └── infrastructure/             # DI, bootstrap, settings
├── tests/                          # Python tests
├── docs/architecture/              # Design docs and ADRs
└── docs/assets/                    # Logo and visual assets
```

## Architecture

All architectural decisions are documented as ADRs in `docs/architecture/adr/`. Read them before making non-trivial changes.

Three principles cut across every layer:

- **Conformance first** — if an operation can't be conformant to the OGC standard, it isn't exposed.
- **By design** — the OpenAPI is built, not pruned. Conformance classes are calculated, not declared.
- **Only async** — zero synchronous code in the critical path.

Other key decisions:

- **DDD with Hexagonal architecture** — clear bounded contexts, ports and adapters
- **Result type** — errors are values (`Result[T, DomainError]`), not exceptions, in domain and application layers
- **Postel's Law** — ABC for internal ports, Protocol for external interfaces
- **dataclass not Pydantic** in the domain — keeps the domain dependency-free

## Code style

- Python: ruff (lint + format), ty
- Rust: cargo fmt, clippy with `-D warnings`
- Sentence case for headings (no Title Case, no ALL CAPS)
- No emoji in code (only in docs where intentional)

## Pull requests

PRs that touch both Rust and Python should be atomic — modify the Rust API, the binding, and the Python wrapper in a single commit. The monorepo layout exists exactly to make this easy (see ADR-017).

Add a CHANGELOG entry under `## [Unreleased]` for any user-visible change.
