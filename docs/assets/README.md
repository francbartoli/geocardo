# Brand assets

The geocardo visual identity is based on Roman urban planning: four *insulae* (building blocks) arranged on a grid defined by the *cardo* (bold vertical axis, traced first) and the *decumanus* (horizontal axis). The four insulae map directly to the four primary bounded contexts: Feature Access, Coverages & Maps, Processing, and Catalogue / Records.

## Files

| File | When to use |
|---|---|
| `logo.svg` | Primary mark. Use at 64px and above, where the cardo/decumanus stripes are legible. Good for documentation, slides, social cards. |
| `logo-lockup.svg` | Mark + "geocardo" wordmark + tagline. Use for README headers, site banners, conference slides — anywhere you want the full identity. |
| `logo-mono.svg` | Monochrome variant for dark backgrounds. Insulae in light teal, cardo stays the primary accent. |
| `favicon.svg` | Simplified — four blocks only, no axes. Use at 16–32px where thin stripes would disappear. |

## Color palette

```
#E1F5EE   Teal 50      Background, light surfaces
#9FE1CB   Teal 100     Accents, decumanus (light)
#1D9E75   Teal 400     Primary, cardo, "geo" in wordmark
#0F6E56   Teal 600     Medium-weight insulae
#085041   Teal 800     Dark insulae, "cardo" in wordmark, text
```

## Typography

The wordmark uses a monospace typeface (`ui-monospace`, falling back to SF Mono / Menlo / Consolas). This reflects the project's developer-tool nature and its alignment with the Astral tooling aesthetic (ruff, uv, ty).

The tagline — **Conformance first. By design. Only async.** — appears in lightweight uppercase with generous letter-spacing.

## Design rationale

The geocardo mark is not a generic geospatial icon. Every element has a specific meaning tied to the project's architecture:

- **Four insulae** — one per bounded context in the DDD decomposition
- **Diagonal color symmetry** (dark / medium / medium / dark) — keeps the grid visually balanced while the four blocks remain distinct
- **Bold vertical cardo** — the primary axis, traced first, corresponds to *conformance* being the first architectural concern
- **Thinner horizontal decumanus** — the secondary axis, corresponds to *intent* (what the operator wants) crossing the standard
- **Small diamond at the intersection** — the ServiceState, the aggregate where standard, intent and capabilities meet

See `docs/architecture/README.md` and the ADR series for the architectural principles these elements represent.
