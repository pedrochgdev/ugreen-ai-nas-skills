# BenchMatch

Help a maker understand the documented differences between two comparable prototype runs and identify what must be recorded before a useful repeat.

Track: **Open Innovation**. Status: **authored Round 1 alternative; official validation pending**.

[Try the existing concept demo](demo.html) · [Proposal PDF](../../deliverables/benchmatch/benchmatch-proposal.pdf) · [Initial Skill ZIP](../../deliverables/benchmatch/benchmatch-initial-skill.zip) · [Skill entry point](skill/benchmatch/SKILL.md)

## End-user workflow

Say: "Run B produced a worse print than A. Compare their records and show what changed and what we still do not know."

1. Select the exact sources and confirm the processing route.
2. Review source-backed findings and incomplete coverage.
3. Answer, skip or change the domain-specific decisions.
4. Approve the complete preview and an exact new destination.
5. Receive the actual write and readback outcomes separately.

The demo is hardcoded, runs offline and does not access NAS data or call a model.
It explains the earlier interaction concept; the Skill documents the full evidence
and execution contract. Its fictional names and identifiers are not runtime inputs.

## What is included

- Original Markdown Skill and six directly linked references.
- English ten-answer proposal, under 500 substantive words, with matching PDF.
- Synthetic authoring fixtures, a user guide, architecture and finalist test plan.
- An initial ZIP containing only the Skill entry point and Markdown references.

## What is not validated yet

The required official creation tool could not be downloaded in this environment.
It has not been installed or used. Exact CLI/action/agent bindings are proposed
until verified against its official catalog; no official static pass is claimed.
Installation and execution on UGREEN AI NAS, real permissions, model locality,
input formats and result semantics remain untested. Local structural checks,
development policy models and the browser demo do not establish those properties.

Do not present this alternative as contest-ready until the official gate in
[SUBMISSION_GUIDE.md](../../SUBMISSION_GUIDE.md) is resolved. Choose only one
project for the hackathon; the four alternatives are not four authorized entries.

## Local checks

From the repository root:

~~~sh
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
~~~

See [proposal source](proposal.md), [user guide](docs/USER_GUIDE.md),
[architecture](docs/ARCHITECTURE.md), [validation](docs/VALIDATION.md) and
[disclosures](skill/benchmatch/references/disclosures.md).
