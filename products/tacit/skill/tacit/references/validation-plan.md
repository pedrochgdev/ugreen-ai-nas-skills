# Validation plan

These are planned target-device tests, not claimed NAS results. Fixtures in
the repository are synthetic authoring data outside the Skill package.

| Case | Setup and request | Acceptance criteria |
| --- | --- | --- |
| Core 1: Special orders handover | Read order-procedure.md, marta-transcript.md and delivery-checklist.md. Identify the unspecified approver and tolerance, then incorporate the user's explicit approver answer. | All settled steps have citations; two initial questions remain distinguishable; a skipped tolerance remains open; no invented numeric limit. |
| Core 2: Authoritative rule conflicts with recording | User designates order-procedure.md as current. Use contradictory-transcript.md. | Supervisor approval and 'ship immediately' are both visible. The affected action stays conflicting until an explicit resolution; it is excluded from teach-back. |
| Edge: Recording unreadable; no process sources | Return an unreadable recording and an empty readable-source inventory. | Explain the empty coverage and stop procedure creation and writes; do not generate a generic SOP. |

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
