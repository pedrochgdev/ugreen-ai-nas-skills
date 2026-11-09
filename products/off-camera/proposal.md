# Off Camera - Round 1 proposal

Track: Bring Memories to Life

## 1. What does the Skill do?

Off Camera prepares a reviewed photo selection representing user-chosen people, with source-linked coverage and conditional exact-selection album creation.

## 2. Target user and problem

Families often have many photographs but few appearances of the person taking them; automatic selections can repeat the same people and moments.

## 3. Proposed solution

Use confirmed identities, scoped photo evidence and an explainable representation heuristic to propose a small selection the family can change.

## 4. Core user flow

Choose people, period, source scope and count; review actual candidates and coverage; replace photos; approve the report and, separately, a supported exact-membership album.

## 5. Substantive difference

The selection exposes representation gaps and preserves exact reviewed membership rather than treating generic similarity or a matching album title as completion.

## 6. UGREEN AI NAS capabilities

Photo discovery and metadata supply confirmed people and capture-time evidence; parent reasoning proposes coverage; text saving records choices; album creation is conditional on supported exact-set semantics.

## 7. Technical approach

The Markdown parent delegates through photo, file and knowledge experts. Catalog bindings remain provisional until official-kit verification. Inputs are typed identities, authorized scope, period and count. Confirm actual model routing before private reads. No external service or custom runtime is added. Codex assisted authoring and local checks.

## 8. Current development status

Implemented: workflow, selection rules, references, fictional candidate records, interactive HTML demo, proposal and local package checks. Official-tool use and validation are blocked by download access. NAS search, identity accuracy, approval behavior and album semantics remain untested; entrant review is pending.

## 9. Final validation plan

Core one: four distinct photos must represent the photographer when evidence permits. Core two: replacing a photo invalidates approval, and an incorrect album member fails verification. Edge: no photographer match must remain an explicit gap without scope expansion.

## 10. Known limitations

Incomplete recognition and stripped capture dates limit coverage. The greedy selection is not globally optimal. Album creation may be unavailable if exact membership cannot be preserved; a reviewed selection report remains the core result.

Substantive response count: 290 words.

## Third-party information

UGREEN tooling and runtime experts: UGREEN terms, no redistribution. No third-party runtime code or model is bundled. Separate demos: Rubik under SIL OFL 1.1. PDF creation: original Python standard-library code. Local checks: pypdf (BSD-3-Clause) and PyYAML (MIT). AI assistance is disclosed in response 7 and the Skill disclosures.
