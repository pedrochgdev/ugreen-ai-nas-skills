---
name: off-camera
description: "Prepare a source-linked photo selection that represents user-chosen people and moments, including a family photographer who appears rarely. Review exact assets and coverage before saving a report or conditionally creating an album."
---

# Goal

Help a family choose a small, reviewable set of real photos that includes the people they want represented, while exposing gaps in the available archive.

Use when the user asks: "Choose four memories from our trip, including Ana, who was usually behind the camera. Let me review the exact photos before creating anything."

# Required input

Exact authorized photo scope and date window; user-confirmed people identifiers or manually identified candidate assets; requested selection size; optional user-defined event labels; optional new report path and album title. Do not infer a person from an unconfirmed face.

Bounds: One authorized folder or album; 2 to 8 user-confirmed people; 4 to 12 requested photos; at most 60 distinct candidate assets and 24 scoped search queries per invocation.

Do not treat the illustrative HTML demo or its fictional identifiers as NAS inputs.

# Generation-time capability evidence

This is an authored candidate. The public Starter Kit was read; the required
official creation tool could not be downloaded, installed or run. Before this
candidate is submitted or installed, the developer must resolve the release gate
in [Capability binding and evidence](references/capability-map.md).

- `ug-photo` → `photo-agent`: proposed binding; official-catalog verification pending.
- `ug-filesystem` → `file-agent`: proposed binding; official-catalog verification pending.
- `ug-knowledge` → `knowledge-agent`: proposed binding; official-catalog verification pending.

No exact CLI/action support, official checker result, local model availability or
NAS runtime success is claimed. Follow the verified catalog after that gate;
an unresolved operation must stop, not be replaced with a script or guessed CLI.

# Orchestration

Read [Execution policy](references/execution-policy.md) for scopes, evidence,
expert delegation, model routing, state transitions, freshness and write approval.
All NAS operations are delegated; the parent only reasons over real returned data.

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

7. Offer album creation only if the installed catalog and photo expert can
demonstrably preserve the exact approved typed asset IDs, ordering when required
and collision policy. The user must separately approve the exact membership and
title, and the platform must authorize creation. A generic search-based album is
not an acceptable substitute for the reviewed selection.

8. Verify the created album's actual returned ID and member IDs through supported
read-only inspection. Report success only for the operation actually verified.
If exact creation or verification is unsupported, say that album creation is
unavailable and keep the reviewed selection report. Unknown write completion
requires inspection before any retry; do not create a duplicate album.


Read [Workflow contract](references/workflow-contract.md) when deriving the result,
and use [Result format](references/result-format.md) for the complete reviewed output.

# Completion and failure

Handle completed, failed, cancelled, waiting_user and waiting_approval exactly as
defined in the execution policy. A partial preview is labeled partial. Empty,
unreadable or unsupported inputs never become inferred evidence. Changing an input
or decision invalidates the affected preview and any previous write approval.
Report preview, user decisions, actual writes and readback as separate outcomes.
Never claim a planned or unverified operation completed.

The developer uses [Validation plan](references/validation-plan.md) for the two
core cases, edge case and assigned NAS session. Source, license, tool and runtime
disclosures are in [Disclosures](references/disclosures.md).
