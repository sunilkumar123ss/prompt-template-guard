# Strict prompt-template renderer

> **Disclosed reconstruction prepared on 24 October 2026.** The recorded Git dates are synthetic, not dates of past development. See [HISTORY.md](HISTORY.md).

This is an incomplete stage in a tutorial reconstruction of an already-completed reference implementation. Source, fixtures, tests, command-line behavior and verification are introduced in later stages. Only the final branch tip contains the complete documented package.

## Intended scope of the final example

Renders a declared set of simple placeholders, rejects attribute/index traversal, conversions, nested format specifications, undeclared fields, and missing/extra variables. Values are rendered once, so braces inside a value cannot introduce another placeholder. This prevents template misuse; it does not make untrusted text safe from prompt injection in a future model call.

All examples are synthetic and educational. This reconstruction does not establish historical employment, deployment, usage, or production benchmarks.
