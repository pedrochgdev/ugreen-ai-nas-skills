# Actual official static-check evidence

Release: **0.2.0**. Review date: 2026-11-09.

The user supplied uliya-skill-kit-0.7.3-en.zip. Its original instructions,
development standard, catalog and checker were used in place. The toolkit and
catalog are not redistributed here. [Provenance](../official-kit.json) records
SHA-256 values for the supplied archive, catalog, checker and checker library.

The reports below are the unmodified JSON output of the actual official
scripts/check-skill.mjs. Each contains the catalog version, diagnostics and
SHA-256 of all seven Markdown files. The repository validator compares those
hashes with current source and checks that each ZIP reproduces that source.

| Skill | Current source | Independent ZIP extraction | Result |
| --- | --- | --- | --- |
| Tacit | [JSON](v0.2.0/source/tacit.json) | [JSON](v0.2.0/extracted-zip/tacit.json) | static-pass; 0 errors, 0 warnings, 0 info |
| Off Camera | [JSON](v0.2.0/source/off-camera.json) | [JSON](v0.2.0/extracted-zip/off-camera.json) | static-pass; 0 errors, 0 warnings, 0 info |
| ContextCut | [JSON](v0.2.0/source/contextcut.json) | [JSON](v0.2.0/extracted-zip/contextcut.json) | static-pass; 0 errors, 0 warnings, 0 info |
| BenchMatch | [JSON](v0.2.0/source/benchmatch.json) | [JSON](v0.2.0/extracted-zip/benchmatch.json) | static-pass; 0 errors, 0 warnings, 0 info |

## Baseline and corrections

The first checks of the provisional, unversioned packages are preserved in
baseline-v0.1.0. Each had zero errors and two warnings: a missing description
trigger and incomplete delegation-workflow static validation. Authoring was then
reconciled with the actual catalog, including concrete registered-agent
delegations and supported document, report-save and photo contracts. Current
reports above supersede that baseline. Old artifacts have not been overwritten.

## Reproduction and limits

With the separate extracted toolkit available:

~~~sh
python3 tools/build_candidates.py --kit /path/to/uliya-skill-kit
python3 tools/validate_repository.py
~~~

Run from the repository root. The builder runs the official checker on source
and fresh ZIP extractions before promoting versioned artifacts. Existing release
files are retained; differing bytes require a new version.

A static pass does not establish device installation, runtime expert behavior,
format support, model locality, permissions, atomic no-replacement saving or
complete album membership enumeration. These remain assigned-NAS validation
items. Optional writes stop when the required guarantees cannot be established;
the reviewed result remains available in the conversation.
