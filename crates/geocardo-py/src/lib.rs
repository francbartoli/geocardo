//! geocardo native bindings.
//!
//! Entry point for the PyO3 extension module exposed to Python as `geocardo._native`.
//!
//! Components will be registered here as the workspace grows:
//!   - geocardo-catalog  -> SpecificationCatalog
//!   - geocardo-cql2     -> parse_cql2_text, parse_cql2_json
//!   - geocardo-schema   -> SchemaValidator
//!   - geocardo-geojson  -> serialize_feature, serialize_feature_collection_stream

use pyo3::prelude::*;

/// Returns the geocardo-py crate version. Sanity check that the native module
/// is built and importable. Replace with real APIs as crates land.
#[pyfunction]
fn _version() -> &'static str {
    env!("CARGO_PKG_VERSION")
}

#[pymodule]
fn _native(_py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(_version, m)?)?;
    Ok(())
}
