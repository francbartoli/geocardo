<p align="center">
  <img src="docs/assets/logo-lockup.svg" alt="geocardo — Conformance first. By design. Only async." width="600"/>
</p>

# geocardo

> **Conformance first. By design. Only async.**

OGC API building blocks for Python. Conformance isn't a goal — it's a structural property.

## Status

🚧 **Pre-alpha** — under active design. APIs are unstable. v0.1 is being built. See [docs/architecture/roadmap.md](docs/architecture/roadmap.md) for the plan.

## What is this

geocardo is an async-native, framework-agnostic Python library for building OGC API services. The OGC specifications themselves are the foundation: a Rust catalog parses the official OGC OpenAPI documents and compiles them into a binary the Python layer queries at runtime. Everything else — domain model, configuration, OpenAPI generation — derives from that catalog.

You write `filterable = true`. geocardo maps your intent to the right OGC specification, verifies your provider supports it, generates the conformant OpenAPI, and validates everything at startup.

## Why

Two roads exist today for OGC API in Python:

- **pygeoapi** — a configurable server. Conformance is declarative. I/O is synchronous.
- **Custom code** — reinvent content negotiation, pagination, link building. Conformance sacrificed to deadlines.

geocardo is a third road: a library, not a server. Async-native. Conformance by construction.

## Foundational principles

- **Conformance first** — if it can't be conformant, it isn't exposed.
- **By design** — the OpenAPI is built, not pruned. Conformance classes are calculated, not declared.
- **Only async** — composes natively with TiPG, Titiler, Obstore, asyncpg, and the rest of the Python/Rust async ecosystem.

## Architecture

Domain-Driven Design with Hexagonal architecture (Ports & Adapters). Python for the domain and orchestration. Rust for hot paths: specification catalog, CQL2 parsing, JSON Schema validation, GeoJSON serialization.

See [docs/architecture/](docs/architecture/) for the full design and the ADR series.

## Quick start

🚧 Not yet — v0.1 is the first usable milestone. Star the repo to follow progress.

For contributors wanting to build from source now, see [CONTRIBUTING.md](CONTRIBUTING.md). Short version:

```bash
git clone https://github.com/francbartoli/geocardo.git
cd geocardo
uv sync          # installs Python, deps, builds the Rust extension
uv run pytest    # verifies the build
```

## Project context

This is a personal project by [Francesco Bartoli](https://github.com/francbartoli). It complements rather than replaces [pygeoapi](https://pygeoapi.io).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Read the ADRs in `docs/architecture/` before making non-trivial changes.

## License

MIT — see [LICENSE](LICENSE).
