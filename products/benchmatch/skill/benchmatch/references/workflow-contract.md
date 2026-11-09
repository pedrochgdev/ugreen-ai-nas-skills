# BenchMatch comparison contract

## Run-bound evidence

Each observation is assigned to one explicitly identified run and process/object
version. It contains a variable, raw value, unit, source key, exact excerpt,
locator when available and reading status. Outcomes are user/source reports,
not facts inferred from a photograph or from parameter changes.

## Classification precedence

1. CONFLICTING: one run has multiple different explicit values for the same
variable and condition, with no documented revision/authority resolving them.
2. UNKNOWN: either run has no readable unambiguous value.
3. NOT_COMPARABLE: dimensions, units, method or context are incompatible and no
explicit supported mapping has been established.
4. MATCH: comparable explicit values agree, or their difference is within an
explicitly user-approved tolerance with units.
5. DIFFERENT: comparable explicit values differ beyond that tolerance.

If no tolerance was supplied, compare the explicit values exactly and describe
the result as a documented difference, not a meaningful physical effect. Keep
raw values beside any normalization. Celsius/Fahrenheit or other conversions
are not assumed; use identical units or a separately confirmed mapping.
Never average conflicts, substitute zero for unknown, or claim a difference from
an unreadable value. The comparison model is a development-only policy example;
the NAS workflow uses expert returns and parent reasoning, not a Python runtime.

## Context and causality

If the user has not established a shared process/object version, show
CONTEXT_REVIEW over the entire comparison. Two changed variables cannot identify
a cause; even one documented difference does not establish causal attribution.
Do not prescribe new temperatures, safety limits or machine settings.

## Next-run checklist and reuse

List variables to record consistently, unresolved source conflicts and the
user's chosen question for a later test. Read a prior report only if explicitly
provided; missing current evidence never means a parameter was unchanged.
Changing source observations or user mappings invalidates previous approval.
