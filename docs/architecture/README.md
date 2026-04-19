# Architecture

geocardo is built on three uncompromising principles, encoded in the codebase rather than just promised in docs:

1. **Conformance first** — if an operation can't be conformant, it isn't exposed.
2. **By design** — the OpenAPI is built, not pruned. Conformance classes are calculated, not declared.
3. **Only async** — zero synchronous code in the critical path.

## Architecture Decision Records

All non-trivial decisions live in [adr/](./adr/). The series:

- ADR-001 — ABC for internal ports, Protocol for external interfaces
- ADR-002 — Plugin discovery preserved via LegacyProviderAdapter
- ADR-003 — Feature as dataclass, not Pydantic
- ADR-004 — Dishka as the DI container
- ADR-005 — Conformance calculated, not declared
- ADR-006 — OpenAPI built, not pruned
- ADR-007 — CC ↔ OpenAPI validation at bootstrap
- ADR-008 — ServiceState immutable, atomic reload
- ADR-009 — Specification versioning in the domain
- ADR-010 — Runtime state source of truth (capability_policy)
- ADR-011 — Intent-driven configuration
- ADR-012 — Format-agnostic configuration with strict JSON Schema
- ADR-013 — Result type for error handling (better-result)
- ADR-014 — Hot reload without downtime
- ADR-015 — Rust components via PyO3
- ADR-016 — Monorepo layout (Rust + Python in one repo)

## Bounded Contexts

geocardo identifies five bounded contexts plus a Shared Kernel:

- **BC1: Feature Access** — Feature, FeatureSet, FeatureQuery, CQL2
- **BC2: Coverage & Maps** — Coverage, TileMatrix, TileSet
- **BC3: Processing** — Process, Job, ExecutionRequest
- **BC4: Catalogue / Records** — Record, RecordQuery
- **BC5: Configuration & Registry** — ServiceState, CollectionRegistration, RegistryBuilder
- **Shared Kernel** — CRS, Link, Extent + SpecificationCatalog + CapabilityIntent/Resolver

Configuration (TOML/YAML/JSON loaders, JSON Schema validation) and OpenAPI generation are **inbound and outbound adapters of BC5** — not bounded contexts of their own. They have no ubiquitous language; they are infrastructure.

## Layout

The Rust workspace lives in `crates/`. The Python package lives in `src/geocardo/`. They are joined via PyO3 + maturin into a single PyPI package. See ADR-017 for the rationale.
