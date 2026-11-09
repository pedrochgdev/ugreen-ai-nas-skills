# Validation plan

These are planned target-device tests, not claimed NAS results. Fixtures in
the repository are synthetic authoring data outside the Skill package.

| Case | Setup and request | Acceptance criteria |
| --- | --- | --- |
| Core 1: Qualification and negation | Use draft.md with ana-transcript.md and leo-transcript.md. | The cafeteria/shipping qualification and lost negation are preserved in two findings. Exact start-year quotation stays separate. Every quote has a source or explicit uncertainty. |
| Core 2: Faithful alternative and source change | Accept an alternative, then alter its source before approved save; also check a completely faithful quotation. | The accepted revision is separate from originals. Changed source invalidates approval. Faithful matched quotation receives no fabricated discrepancy. |
| Edge: Missing or ambiguous source | Remove leo-transcript.md or provide two possible speakers for the same sentence. | The affected quotation is UNVERIFIED or requires attribution clarification; no source passage, timestamp or all-clear result is invented. |

## Assigned NAS day

1. Record official tool/catalog and device versions, actual model routes and
registered expert contracts. Use only fictional or authorized test content.
2. Import the selected Skill through the officially supported process and
verify it can be invoked. A local HTML demo is not installation evidence.
3. Execute the two core cases and edge case above. Capture actual expert
outputs, source locators, coverage and approval behavior; record failures.
4. Repeat with a declined write, destination collision, changed source,
interrupted write and readback failure. Verify no unapproved changes and no
duplicate retry. Check source files remain unchanged using supported evidence.
5. Measure time-to-preview and expert call count on the bounded fixture set.
Do not publish a performance claim before measuring it.
6. Record an English-narrated demonstration under three minutes on the
assigned NAS. Export permitted logs, fixtures and video before access expires.

## Evidence levels

- Structural/generic checks establish only file and metadata properties.
- Development policy-model tests exercise selected rules outside the NAS.
- A paper walkthrough assesses instruction coherence.
- Official static checks require the actual official tool.
- Runtime success requires the assigned UGREEN environment.
Report these levels separately; none substitutes for the next.
