---
name: contextcut
description: "Review up to three draft interview quotations against authorized full transcripts, identify omitted conditions, lost negations or attribution changes, and prepare source-linked alternatives for an editor's approval. Do not edit or render media."
---

# Goal

Help an editor preserve the supported meaning of interview material while preparing a shorter script from private NAS sources.

Use when the user asks: "Check these three quotations in my short script against the complete interviews. Show any omitted qualification and let me approve an alternative."

# Required input

Draft file or exact quotation list; authorized full transcript files; source/speaker mapping if known; editing language; optional selected recording; optional new report path. Timestamps and page locators are optional evidence, not guaranteed outputs.

Bounds: At most three draft quotations, six selected readable transcripts and one optional supported audio recording. Bound context to the relevant question/answer and adjacent passages; request narrower sources when extraction limits are reached.

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

1. Confirm the exact draft, at most three quoted excerpts, authorized full
sources, speaker mapping, output language and processing route. Ask the user to
resolve multiple possible drafts rather than choosing by filename or modification
time. Preview-only mode requires no output path.

2. Delegate bounded inventory and freshness metadata to file-agent. Return exact
paths, type, reading status and coverage. Do not search other projects for a
matching sentence. If the draft or all full sources are unavailable, explain the
missing inputs and stop the unsupported comparison.

3. Delegate draft extraction and source-context lookup to document-agent.
Include the actual draft excerpts and selected full-source paths. Ask for the
exact matching passage, speaker attribution, surrounding question and answer,
actual returned locators, match ambiguity and unreadable-source accounting.
First seek verbatim correspondence. If a cut contains a deletion or substitution,
the expert may establish a source-anchored edit alignment using a user-nominated
source/speaker and distinctive literal anchors. Require both raw passages, the
explicit alignment and uniqueness/attribution evidence. This supports reviewing
a lost negation without labeling the altered cut EXACT. A plausible paraphrase
alone is insufficient; unresolved or multiple possible alignments stay UNVERIFIED.

4. If explicitly selected and supported, ask knowledge-agent to transcribe the
recording. Preserve actual returned text and any offsets; uncertain words or
negations remain review items. If audio is unsupported, request a readable
transcript. Do not introduce a conversion executable or arbitrary video processing.

5. Apply workflow-contract.md to classify every quotation separately. A missing
or repeated ambiguous match is UNVERIFIED. For an established match, examine
negation, scope, conditions, exceptions, time, attribution and source uncertainty.
Distinguish EXACT from a semantic review finding; the Skill is not a truth detector.

6. Present draft quotation, original passage, source path, actual locator if any,
review reason and a proposed source-supported alternative. Alternatives use
contiguous source text or clearly labeled separate fragments; do not splice
speakers or disconnected clauses into an apparently verbatim new quotation.
Translation is a labeled paraphrase, not a verbatim quotation.

7. The editor may accept an alternative, retain the original draft with a note,
or leave the item unresolved. Save these decisions for every quotation, including
the items not currently displayed. A user preference cannot verify a missing source.
The source interviews and draft files remain unchanged; the report contains a
separate proposed revised-excerpt section.

8. Assemble result-format.md. Recheck source identity/freshness, invalidate stale
decisions, show the complete report and new destination, then follow the shared
approved create-only save and independent readback rules. No media is cut, rendered,
uploaded or published by this workflow.


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
