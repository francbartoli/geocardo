"""Sanity tests: project is importable, native module behaves predictably."""

import geocardo


def test_version_is_set() -> None:
    assert geocardo.__version__ == "0.0.0"


def test_has_native_returns_bool() -> None:
    """has_native() must return a bool.

    In a correctly-built install (via `maturin develop` or a PyPI wheel),
    this returns True. It returns False only when the compiled extension
    is missing, which indicates a broken build rather than a supported
    fallback mode.
    """
    assert isinstance(geocardo.has_native(), bool)


def test_native_version_matches_when_available() -> None:
    """
    If the native module is present, its version matches the package version.
    """
    if not geocardo.has_native():
        return
    from geocardo import _native  # ty: ignore[unresolved-import]

    assert _native._version() == geocardo.__version__
