# Selecting and promoting one candidate

## Choose one

Only one project may be submitted by an entrant/team. Keep the other alternatives
as research or concepts. The source repository itself is not a required Round 1
deliverable and is not a Skill ZIP.

## Official authoring and static validation completed

Release 0.2.0 uses the user-supplied UGOS toolkit 0.7.3 and its Uliya standard and
catalog 2.0.0. CLI/action/expert mappings and relevant argument/output contracts
were reconciled with the actual catalog. The actual checker reports static-pass,
zero diagnostics on each source folder and each independent ZIP extraction.
See [raw reports and provenance](validation/official/README.md).

Reproduce with a separate copy of the official toolkit:

~~~sh
python3 tools/build_candidates.py --kit /path/to/uliya-skill-kit
python3 tools/validate_repository.py
~~~

The builder runs scripts/check-skill.mjs from that toolkit; this repository does
not redistribute or recreate the checker. It preserves immutable release files.
Revisions require a new version, regenerated PDF/ZIP files and fresh actual
checker reports. Static success does not resolve catalog properties marked
unknown or establish assigned-device behavior. Entrant review of AI-assisted
text, rights, eligibility and declarations remains necessary before submission.

## Round 1 artifacts

For the single chosen product, use its separate files in deliverables/PRODUCT/v0.2.0/,
linked from the [main README](README.md). Unversioned files are historical
provisional artifacts and should not be selected instead:

- The English proposal PDF, at most 1 MB. It answers all ten required questions;
  substantive answers stay under 500 words in total.
- The initial Skill ZIP, at most 10 MB compressed and uncompressed, with at most
  100 files and at most 1 MB per file. It contains only SKILL.md and directly linked
  references/*.md under the named Skill directory.

Do not place HTML, PDF, test fixtures, scripts, repository metadata or a manifest
inside that ZIP. No NAS access, runtime screenshot, public repository or video is
required for Round 1. The official deadline published at preparation is
November 15, 2026, 11:45 p.m. PST; verify the event page before submitting.

## Finalist work

Use the assigned testing day for supported installation, exact expert round trips,
input compatibility, routing, permissions, error handling and real results.
Confirm save-text's actual returned path, independent text readback and whether
the expert can guarantee no replacement; otherwise retain preview-only output.
For Off Camera, verify exact add-item binding and complete member enumeration
scoped to the returned album identity before claiming exact album creation.
Run the two core tests and edge case documented by the selected product.
Record actual English narration/subtitles and NAS footage in a video under
three minutes, uploaded publicly to YouTube as required by the rules.

The Round 2 project must be the same project entered in Round 1. Back up permitted
artifacts before the assigned account expires. This repository does not fabricate
a final video, device logs or a claim that NAS testing has already occurred.

## Authoritative sources

- [Official rules](https://ugreenhackathon.devpost.com/rules)
- [Submission requirements](https://ugreenhackathon.devpost.com/)
- [Official Starter Kit](https://ai.ugreen.com/pages/hackathon-starter-kit)
