# Validation plan

These are planned target-device tests, not claimed NAS results. Fixtures in
the repository are synthetic authoring data outside the Skill package.

| Case | Setup and request | Acceptance criteria |
| --- | --- | --- |
| Core 1: Represent the photographer | Use candidate-photos.json. Request four photos covering Ana, Diego, Lucia and Sofia; compare the starting selection F01-F04 with the proposed selection. | Exactly four distinct real fixture IDs, Ana represented if feasible, selected coverage recomputed, no manufactured photograph. |
| Core 2: User replacement and exact membership | Replace one proposed asset, approve the new exact set and request an album. Simulate an album expert returning a different member ID. | The approval applies only to the current set. A membership mismatch is reported as unverified; a matching count alone does not pass. |
| Edge: No Ana photos in available scope | Use only F01-F04 and keep Ana as a priority. | Explicitly show no confirmed Ana match in checked material. Do not substitute another person or expand scope; obtain agreement before changing the goal. |

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
