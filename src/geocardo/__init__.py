"""geocardo — OGC API building blocks.

Conformance first. By design. Only async.
"""

__version__ = "0.0.0"


def has_native() -> bool:
    """Return True if the compiled native module is importable.

    geocardo depends on compiled Rust components via `maturin develop` (local)
    or the wheels published to PyPI (distributed installs). This helper is
    primarily a diagnostic used by tests and the CLI to verify the build, not
    a real fallback mechanism.
    """
    try:
        import geocardo._native  # ty: ignore[unresolved-import]  # noqa: F401
    except ImportError:
        return False
    return True
