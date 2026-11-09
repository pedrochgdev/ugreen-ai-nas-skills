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

The parent delegates ug-filesystem discovery/verification to file-agent, ug-document qa/reconcile to document-agent, and ug-knowledge transcription/save-text to knowledge-agent. Actual passages and attribution ground review. Inputs include draft and authorized sources. Confirm model routing; prefer local processing. Each write requires approval. No media editing or external API is bundled. Codex assisted development.

## 8. Current development status

Implemented: original Markdown workflow, references, synthetic fixtures, concept demo, proposal and local checks. UGOS Skill Creation Tool 0.7.3 and catalog 2.0.0 were used to reconcile authoring; official static reports accompany the release. NAS installation, execution, extraction accuracy and model routing remain untested. Entrant review is pending.

## 9. Final validation plan

Core one: detect a removed shipping exception and negation with exact source context. Core two: preserve a faithful quote and invalidate approval after source changes. Edge: missing or ambiguous attribution must remain unverified without invented text or timestamps.

## 10. Known limitations

Semantic interpretation and transcription may be wrong; editorial review remains human. Locator availability depends on experts. The Skill produces reviewed text and never cuts, renders or publishes media.

Substantive response count: 289 words.

## Third-party information

UGREEN tooling and runtime experts: UGREEN terms, no redistribution. No third-party runtime code or model is bundled. Separate demos: Rubik under SIL OFL 1.1. PDF creation: original Python standard-library code. Local checks: pypdf (BSD-3-Clause) and PyYAML (MIT). AI assistance is disclosed in response 7 and the Skill disclosures.
