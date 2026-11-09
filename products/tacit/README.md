# Tacit

Help a replacement worker understand a recurring office or workshop process without turning an informal explanation into unsupported instructions.

Track: **Automate Your Workflow**. Release: **0.2.0**.
Official static checks pass with zero errors and warnings, both for source and
an independent extraction of the ZIP. NAS execution is still pending.

[Concept demo](demo.html) · [Proposal PDF](../../deliverables/tacit/v0.2.0/tacit-proposal.pdf) · [Skill ZIP](../../deliverables/tacit/v0.2.0/tacit-initial-skill.zip) · [Entry point](skill/tacit/SKILL.md)

## User journey

Say: "Marta is away next week. Document how she prepares special orders and show me what her replacement still needs to ask."

1. Confirm the real source selection, goal and processing route.
2. Inspect cited evidence and coverage from registered experts.
3. Resolve, skip or change the domain decisions.
4. Review the complete result and approve each optional write separately.
5. Receive the real output identifier and verification outcome.

The HTML demo is the earlier hardcoded interaction prototype. Its fictional
records and identifiers are not live NAS inputs or evidence that the Skill ran.

## Official-tool evidence

The supplied UGOS Skill Creation Tool 0.7.3 and catalog 2.0.0 were read and used
to reconcile this original workflow. Exact CLI-to-agent mappings, published action
names and effects were checked. The actual checker diagnostics, file SHA-256
values and catalog/checker hashes are preserved in validation/official/.

The developer tools are not redistributed. See [evidence](../../validation/official-kit.json)
and [submission guide](../../SUBMISSION_GUIDE.md). The earlier unversioned ZIP/PDF
is retained as the initial provisional candidate; use the linked v0.2.0 release.

## What is included

The Skill and six linked Markdown references; English ten-answer proposal and
matching PDF under the word/size limits; synthetic authoring fixtures; user guide;
architecture; two core tests and an edge case; concept demo and video outline.
The Skill ZIP contains only the named Skill directory and Markdown instructions.

## Remaining validation

Static checks do not prove installation, live permissions, model locality,
supported document formats, extraction quality, exact album behavior or device
execution. The catalog itself marks permissions, prerequisites, error codes and
stability unknown. Test these on the assigned NAS and review entrant declarations.
Only one alternative may be entered by the same entrant or team.

## Rebuild and verify

~~~text
python3 tools/build_candidates.py --kit /path/to/uliya-skill-kit
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
~~~

The first command uses the actual toolkit and refuses a changed existing release.
The repository checks remain distinct from official checks and NAS validation.

[User guide](docs/USER_GUIDE.md) · [Architecture](docs/ARCHITECTURE.md) · [Tests](docs/VALIDATION.md) · [Disclosures](skill/tacit/references/disclosures.md)
