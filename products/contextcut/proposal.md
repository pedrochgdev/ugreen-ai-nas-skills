# ContextCut - Round 1 proposal

Track: Unleash Your Creativity

## 1. What does the Skill do?

ContextCut reviews draft interview quotations against authorized complete transcripts and prepares source-linked editorial warnings and alternatives.

## 2. Target user and problem

Editors and small documentary teams need shorter scripts while preserving qualifications, negations and attribution in private, unpublished interviews.

## 3. Proposed solution

Match each draft quotation to its actual source context, flag supported changes in apparent meaning and let the editor decide on a faithful alternative.

## 4. Core user flow

Select draft and transcripts; authorize scope and processing; review each quotation; accept, retain or leave unresolved; approve a separate report.

## 5. Substantive difference

The workflow targets meaning lost during quotation selection, preserves unresolved attribution and records every editor decision alongside evidence.

## 6. UGREEN AI NAS capabilities

File discovery establishes the source set and freshness; document lookup and reconciliation retrieve context; optional supported transcription adds evidence; approved text saving preserves the review.

## 7. Technical approach

A Markdown parent delegates to file, document and knowledge experts and reasons over actual returned passages. Inputs include draft, sources and speaker mapping. Proposed CLI bindings need official-kit verification. Confirm model routing before private reads; prefer a verified local route. No media editing or external API is included. Codex assisted development.

## 8. Current development status

Implemented: complete workflow, review rules, references, synthetic transcripts, HTML concept demo, proposal and local package checks. Official-tool use and validation remain blocked by download access; NAS execution, extraction and permissions are untested. Entrant review is pending.

## 9. Final validation plan

Core one: detect a removed shipping exception and negation with exact source context. Core two: preserve a faithful quote and invalidate approval after source changes. Edge: missing or ambiguous attribution must remain unverified without invented text or timestamps.

## 10. Known limitations

Semantic interpretation and transcription may be wrong; editorial review remains human. Locator availability depends on experts. The Skill produces reviewed text and never cuts, renders or publishes media.

Substantive response count: 274 words.

## Third-party information

UGREEN tooling and runtime experts: UGREEN terms, no redistribution. No third-party runtime code or model is bundled. Separate demos: Rubik under SIL OFL 1.1. PDF creation: original Python standard-library code. Local checks: pypdf (BSD-3-Clause) and PyYAML (MIT). AI assistance is disclosed in response 7 and the Skill disclosures.
