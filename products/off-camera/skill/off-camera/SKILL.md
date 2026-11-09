---
name: off-camera
description: "Reviewed family-photo selections with explicit person coverage when a user wants the family photographer or other chosen people represented."
---

# Goal

Help a family choose a small, reviewable set of real photos that includes the people they want represented, while exposing gaps in the available archive.

Use when the user asks: "Choose four memories from our trip, including Ana, who was usually behind the camera. Let me review the exact photos before creating anything."

# Required input

Exact authorized photo scope and date window; user-confirmed people names, or manually identified candidate assets; let photo-agent resolve actual typed identities; requested selection size; optional user-defined event labels; optional new report path and album title. Do not infer a person from an unconfirmed face.

Bounds: One authorized folder or album; 2 to 8 user-confirmed people; 4 to 12 requested photos; at most 60 distinct candidate assets and 24 scoped search queries per invocation.

Fictional demo records are not NAS inputs. Experts resolve their own private
options from the user's business goal; do not request hidden parameters upfront.

# Generation-time capability evidence

Authoring uses the supplied official UGOS Skill Creation Tool 0.7.3 and catalog
2.0.0. The declared unique mappings and selected actions were read from that
catalog. See [Capability evidence](references/capability-map.md) for exact actions,
effects, approval and limitations. This evidence does not prove NAS execution.

- `ug-filesystem` → `file-agent`
- `ug-photo` → `photo-agent`
- `ug-knowledge` → `knowledge-agent`

# Orchestration

Read [Execution policy](references/execution-policy.md) for authorization, model
routing, evidence, all delegation states, freshness, collisions and verification.
The parent uses only standard delegation for NAS work and reasons over real
upstream business results. Never dispatch incomplete or unresolved instructions.

1. Confirm people, source scope, date window, requested count and processing
route. Ask for confirmation of any ambiguous person identifier. Person labels
come from the user or confirmed platform identities, never demographic inference.

2. Delegate scoped photo discovery to photo-agent with the exact scope, person
identifiers, period, 24-query limit and 60-distinct-candidate limit. Ask for typed
asset IDs, actual paths when available, capture time status, confirmed people,
event labels when returned and result coverage. Filter every returned asset
against the approved scope. If the search cannot enforce or verify scope, stop.

3. Build a candidate evidence table from completed results. A missing face result
means unknown presence, not absence. Discard duplicate asset IDs. Deduplicate
separate files by content only if a supported expert actually returns matching
content evidence; otherwise label duplicate status unverified.

4. Apply workflow-contract.md to propose a small selection. Maximize useful
representation using the documented greedy rule, and label it a heuristic rather
than a proven optimum. If too few candidates exist, offer a reduced count for
explicit agreement. Show people with no verified match without substituting
another person or another time window.

5. Show the exact proposed asset IDs, their sources, reasons and person coverage.
Allow the user to replace assets or change priorities. Recompute coverage after
each change. Do not describe who attended the real trip from archive coverage.
Do not infer a family relationship, mood, health condition or protected attribute.

6. Offer a reviewed report as the core output. Read result-format.md and follow
the separate approved create-only save/readback procedure. A declined save leaves
the preview available without writing.

7. Offer album creation only if the photo expert can
demonstrably preserve the exact approved typed asset IDs using the documented repeatable add-item capability, ordering when required
and collision policy. The user must separately approve the exact membership and
title, and the platform must authorize creation. A generic search-based album is
not an acceptable substitute for the reviewed selection.

8. Verify the created album's actual returned ID and member IDs through supported
read-only inspection. Report success only for the operation actually verified.
If exact creation or verification is unsupported, say that album creation is
unavailable and keep the reviewed selection report. Unknown write completion
requires inspection before any retry; do not create a duplicate album.


Catalog-specific album boundary: create-album-custom accepts an album name but
has no explicit item-selection parameter in this catalog. It is not a substitute
for exact membership. Use the registered photo expert with create-album only if
it can bind the approved typed assets to the actual add-item contract. Verify
members through search-picture scoped to the returned album_uuid; album-detail
alone promises album/people details, not a complete typed member list. If exact
binding or membership readback is unavailable, keep the reviewed report and say
the album was not created or its membership remains unverified.


## Standard expert delegations

Use the following tasks at the corresponding workflow stages, not as one
unconditional sequence. Uppercase bindings name actual business values.
SOURCE_SCOPE and limits come from the user; paths, source identities and
typed asset IDs come only from completed upstream results. APPROVED_REPORT,
OUTPUT_DIRECTORY, FILENAME_HINT and album choices require current consent.
VERIFIED_OUTPUTFILE and VERIFIED_ALBUM_UUID come only from real successful
expert responses. Replace every named binding with the full actual value
inside each instruction before dispatch; a missing value stops its step.
Preserve all quoting as one supported delegation argument. Do not send
binding names literally or rely on shared expert memory.

### Source verification

`delegate --target file-agent --instruction 'Inspect only the authorized SOURCE_SCOPE for SOURCE_SELECTION. Preserve the selected entities and limits in RUN_LIMITS. Return actual paths, file kinds, identity metadata, readable coverage and bounded plain text when appropriate. Keep read-only; if no results are found return an empty result without widening scope.'`

### Photo evidence

`delegate --target photo-agent --instruction 'Within PHOTO_SCOPE and PERIOD resolve the user confirmed PEOPLE without guessing identities. Return at most CANDIDATE_LIMIT real typed assets, capture-time status, confirmed person matches, available moment labels and coverage. Use only verified scope; an empty result stops this branch. Return ambiguity for user review.'`

### Freshness and collision review

`delegate --target file-agent --instruction 'Recheck only SOURCE_IDENTITIES and the authorized OUTPUT_DIRECTORY for the reviewed FILENAME_HINT. Return actual source fingerprints or metadata and any collision evidence. Keep read-only. Report changed or unverifiable inputs explicitly; do not authorize an overwrite or infer exclusive-create behavior.'`

### Separately approved save

`delegate --target knowledge-agent --instruction 'After the explicit user approval for APPROVED_REPORT and OUTPUT_DIRECTORY with FILENAME_HINT, save only that exact text through the approved workflow. Never replace an existing report. If no-replacement cannot be enforced stop without writing. Return completed state and actual verified, outputFile and contentBytes or a truthful pending, partial or failure result.'`

### Independent readback

`delegate --target file-agent --instruction 'Read only the actual VERIFIED_OUTPUTFILE returned by the completed save within OUTPUT_DIRECTORY. Return the complete saved text and identity evidence for comparison with APPROVED_REPORT. Do not write or broaden scope. An unreadable or partial result means readback is incomplete.'`

### Optional separately approved album

`delegate --target photo-agent --instruction 'After the separate user approval of APPROVED_TYPED_ASSETS and ALBUM_TITLE, create only that exact set through supported album creation if item binding and no-replacement can be honored. Stop on unsupported or ambiguous membership. Return actual album_uuid and completion state. Never substitute a search-based set.'`

### Album membership inspection

`delegate --target photo-agent --instruction 'Inspect only VERIFIED_ALBUM_UUID returned by the completed creation. Return actual typed member identities and coverage through a scoped supported photo query. Keep read-only. If membership cannot be enumerated completely report verification incomplete rather than claiming an exact match.'`


Read [Workflow contract](references/workflow-contract.md) for the domain rules.
Use [Result format](references/result-format.md) for the complete reviewed output.

# Completion and failure

Handle completed, failed, cancelled, waiting_user and waiting_approval as distinct
states. Only a completed expert result supports dependent operations. If no
results are found, state the empty result and stop that branch without widening
scope or substituting another source. Preserve useful partial results with their
limitations. A changed source, goal or decision invalidates affected approval.
Report preview, each actual write and readback as separate outcomes.

Use [Validation plan](references/validation-plan.md) for core cases, edge case
and assigned-device testing. Read [Disclosures](references/disclosures.md) for
rights, sources, AI assistance and the distinction between static and NAS checks.
