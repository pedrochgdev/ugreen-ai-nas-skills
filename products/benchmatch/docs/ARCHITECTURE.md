# BenchMatch: architecture

## Execution model

User request and scoped authorization -> registered-expert reads -> checked
evidence records -> parent domain reasoning -> human review -> separately approved
write -> readback. No standalone application server or custom NAS runtime exists.

The Skill entry point supplies the workflow. execution-policy.md defines shared
states and evidence handling; workflow-contract.md carries the domain decisions;
result-format.md specifies the artifact. All six references are directly linked
from SKILL.md. The package has no separate manifest, executable or dependency bundle.

## State model

Collect -> verify capabilities/route -> discover -> extract -> derive -> review ->
approve -> write -> verify. Empty/failed/unknown states stop dependents. Partial
coverage remains visible. Changes return the affected work to review and invalidate
approval. An uncertain write enters inspection, not automatic retry.

## Capability boundary

The exact proposed registry and CLI bindings are documented as unverified in
capability-map.md. The public official guide establishes families, not schemas.
The official tool/catalog gate is unresolved; it must be reconciled before
installation or submission. Optional capabilities fail explicitly.

## Persistence and data

Sources remain in authorized NAS storage; reports use a new approved path.
Previous reports are read only when explicitly supplied. There is no implicit
database, scheduled process or background watcher. Model routing must be checked
for parent reasoning and experts, including any cloud processing.

## Presentation and tests

The HTML demo simulates the user interaction. Synthetic fixtures contain no real
personal data. Development-only reference models exercise selected policy rules
outside Uliya. Structural checks inspect ZIP/PDF properties. None executes NAS
experts or proves model accuracy, installation, permissions or locality.
