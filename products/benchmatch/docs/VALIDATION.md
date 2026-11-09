# Validation plan

These are planned target-device tests, not claimed NAS results. Fixtures in
the repository are synthetic authoring data outside the Skill package.

| Case | Setup and request | Acceptance criteria |
| --- | --- | --- |
| Core 1: Two parameter changes plus missing humidity | Use run-a.md and run-b.md; compare temperature, speed, material, lot and humidity. | Temperature and lot differ; speed/material match; humidity is UNKNOWN. No causal explanation or missing value is invented. |
| Core 2: Additional note and conflict | User links humidity-b.md to B, then include conflicting-b.md. | Humidity becomes 45 percent with its note source. Two incompatible B temperatures produce CONFLICTING, not an average or arbitrary winner. |
| Edge: Different units or unknown run identity | Provide an unassigned run note or Fahrenheit value against Celsius without a confirmed mapping. | NOT_COMPARABLE or CONTEXT_REVIEW remains visible; no guessed conversion, zero or causal verdict. |

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
