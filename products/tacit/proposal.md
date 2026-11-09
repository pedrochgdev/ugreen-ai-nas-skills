# Tacit - Round 1 proposal

Track: Automate Your Workflow

## 1. What does the Skill do?

Tacit turns an authorized expert explanation and operating documents into a traceable handover procedure, clarification queue and teach-back exercise.

## 2. Target user and problem

Small workshops and teams lose practical knowledge when experienced staff are absent; recordings and procedures often omit owners, exceptions and decision rules.

## 3. Proposed solution

Reconcile documented steps with an optional recording, retain disagreements, ask precise missing-fact questions and build source-backed learning checks.

## 4. Core user flow

Choose process and sources; authorize processing; review evidence and questions; answer or skip; try the exercise; approve a new report.

## 5. Substantive difference

Tacit operationalizes gaps in tacit knowledge: unresolved conditions remain visible and cannot silently become instructions or correct quiz answers.

## 6. UGREEN AI NAS capabilities

File discovery establishes scope; document reading and reconciliation extract procedure evidence; supported transcription adds spoken context; approved text saving preserves the reviewed handover.

## 7. Technical approach

The Markdown parent delegates ug-filesystem work to file-agent, ug-document qa/reconcile to document-agent, and ug-knowledge transcription/save-text to knowledge-agent. Real upstream evidence drives each step. Inputs specify process, scope, authority and learner. Verify model routing before private reads; prefer local processing. Writes require separate approval. Codex assisted development.

## 8. Current development status

Implemented: original Markdown workflow, references, synthetic fixtures, concept demo, proposal and local checks. UGOS Skill Creation Tool 0.7.3 and catalog 2.0.0 were used to reconcile authoring; official static reports accompany the release. NAS installation, execution, extraction accuracy and model routing remain untested. Entrant review is pending.

## 9. Final validation plan

Core one: recover missing approver and tolerance without inventing either. Core two: preserve a current procedure's conflict with a recording and exclude it from settled teaching. Edge: unreadable recording with no readable sources must produce no procedure or write.

## 10. Known limitations

Depends on supported experts, readable sources and confirmed model routing. Transcription may misread important words; a handover report does not certify practical competence. No custom runtime or external API is bundled.

Substantive response count: 289 words.

## Third-party information

UGREEN tooling and runtime experts: UGREEN terms, no redistribution. No third-party runtime code or model is bundled. Separate demos: Rubik under SIL OFL 1.1. PDF creation: original Python standard-library code. Local checks: pypdf (BSD-3-Clause) and PyYAML (MIT). AI assistance is disclosed in response 7 and the Skill disclosures.
