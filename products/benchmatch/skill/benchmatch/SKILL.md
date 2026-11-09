---
name: benchmatch
description: "Compare documented conditions of two authorized workshop or prototyping runs, preserve missing or conflicting parameters, and prepare a reviewed difference report with a next-run recording checklist. Do not infer causality or control equipment."
---

# Goal

Help a maker understand the documented differences between two comparable prototype runs and identify what must be recorded before a useful repeat.

Use when the user asks: "Run B produced a worse print than A. Compare their records and show what changed and what we still do not know."

# Required input

Exact source files and scope for run A and B; process/object/version identity confirmed by the user; variables and units to compare; any user-defined tolerances; user-reported outcomes; optional additional note and report path.

Bounds: Two named runs of one user-confirmed process/object version; at most eight source documents, twelve requested variables and one optional supported recording per invocation.

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

1. Ask the user to identify both runs, the shared process/object version,
source scope, variables, explicit units, outcome provenance and any tolerances.
Do not compare clinical or hazardous operating procedures through this workshop
workflow. Confirm the actual processing route before reading private prototype IP.

2. Delegate bounded discovery to file-agent with exact run source lists and
eight-document/one-recording limits. Return source identity, declared run, actual
path, readability and coverage. A filename alone is insufficient to assign a
document to a run; ask for the user's confirmation when the record is ambiguous.

3. Delegate extraction to document-agent with actual source paths and the
requested variable list. Return run identity, variable, printed value, unit,
source excerpt, locator if available, reading status and all conflicting
observations. A note for a different part/version is not silently merged.

4. If explicitly selected and supported, delegate a run-note recording to
knowledge-agent. Preserve uncertainty and actual offsets; ask for text if that
audio type is unsupported. Keep an additional note separate until its run
identity and source relationship are established.

5. Establish whether the two runs have the user-confirmed comparable context.
If process/object/version differs or remains unknown, report the comparison as
CONTEXT_REVIEW. Do not describe it as a controlled experiment. The user may
clarify the context, with that assertion retained as such.

6. Apply workflow-contract.md per variable: MATCH, DIFFERENT, UNKNOWN,
CONFLICTING or NOT_COMPARABLE. Preserve raw values and units. Use only explicitly
supported unit normalization and declared tolerances; request clarification for
ambiguous units, precision or mappings. Do not guess a missing humidity or
resolve two conflicting temperatures by averaging.

7. Show the difference table and source-linked gaps. The user may add a scoped
note, correct an interpretation or leave a value unknown. Recompute affected
rows while preserving the source and user-decision trail. Suggest a recording
checklist for the next run, not an equipment adjustment or causal conclusion.

8. Assemble result-format.md with reported outcomes kept separate from parameter
observations. Recheck source freshness and follow the shared approved create-only
save/readback rules. Do not operate equipment, execute experiments or start a
resident monitoring task.


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
