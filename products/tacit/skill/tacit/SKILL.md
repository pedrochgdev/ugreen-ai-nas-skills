---
name: tacit
description: "Turn an authorized expert recording and selected operating documents into a source-linked procedure, precise clarification questions and a teach-back exercise. Use for knowledge handovers; keep unresolved roles and conflicting instructions visible."
---

# Goal

Help a replacement worker understand a recurring office or workshop process without turning an informal explanation into unsupported instructions.

Use when the user asks: "Marta is away next week. Document how she prepares special orders and show me what her replacement still needs to ask."

# Required input

Process name; exact source files or folder; optional recording; the user-designated authoritative procedure and version, if any; intended learner; output language; optional new report destination. A source's modification time does not establish authority.

Bounds: One named process; at most 12 selected documents and one supported audio recording per invocation. Ask for a narrower scope if extraction exceeds the expert's supported limits.

Do not treat the illustrative HTML demo or its fictional identifiers as NAS inputs.

# Generation-time capability evidence

This is an authored candidate. The public Starter Kit was read; the required
official creation tool could not be downloaded, installed or run. Before this
candidate is submitted or installed, the developer must resolve the release gate
in [Capability binding and evidence](references/capability-map.md).

- `ug-filesystem` → `file-agent`: proposed binding; official-catalog verification pending.
- `ug-document` → `document-agent`: proposed binding; official-catalog verification pending.
- `ug-knowledge` → `knowledge-agent`: proposed binding; official-catalog verification pending.

No exact CLI/action support, official checker result, local model availability or
NAS runtime success is claimed. Follow the verified catalog after that gate;
an unresolved operation must stop, not be replaced with a script or guessed CLI.

# Orchestration

Read [Execution policy](references/execution-policy.md) for scopes, evidence,
expert delegation, model routing, state transitions, freshness and write approval.
All NAS operations are delegated; the parent only reasons over real returned data.

1. Confirm the named process, source scope, learner and processing route.
Record the user's authoritative source/version choice as AUTHORITY, or record
"authority not designated"; do not select an authority yourself.

2. Delegate bounded discovery to file-agent. Include the actual SOURCE_SCOPE,
12-document and one-recording limits, allowed source types, no scope expansion,
and required return fields: exact path, type, identity metadata, readability and
coverage. Stop if no eligible source is found. Ask the user to select among
multiple recordings or ambiguous process folders.

3. Delegate source reading to document-agent with the exact selected files.
Return atomic observations: step/action, actor, trigger, condition, limit,
exception, sequence, exact excerpt and actual locator. Independently label each
field explicit, missing, unreadable or conflicting. Do not create a mandatory
step merely because it is common practice.

4. If the user selected a supported recording, delegate transcription to
knowledge-agent. Return the actual transcript and offsets only when provided.
Mark uncertain negations, names and quantities for review. If transcription is
unavailable, continue from a user-selected readable transcript or stop that branch.
Never extract audio from video through an unlisted conversion path.

5. Reconcile atomic observations using workflow-contract.md. Preserve an
authoritative instruction beside a conflicting informal instruction; do not
silently merge them. Draft the supported procedure and up to five targeted
clarification questions. When no authority is designated, present competing
instructions without choosing one as the process.

6. Present the procedure, evidence, unknowns and question queue. Record each
answer as a dated user decision linked to the affected step. A skipped question
stays open. If the user resolves a contradiction, retain both source claims and
their explicit resolution rather than erasing the history.

7. Offer up to three teach-back questions whose answers are supported and
uncontested. A reply is compared against the cited procedure, with explanatory
feedback. Do not score answers that depend on unresolved rules. The exercise
checks the documented process, not physical competence or safety certification.

8. Assemble result-format.md, including unresolved questions and a repeat-use
change summary only if the user explicitly supplies an earlier report. Do not
use implicit session memory as a persistent database. Offer preview-only output
or follow the approval, create-only save and readback sequence in execution-policy.md.


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
