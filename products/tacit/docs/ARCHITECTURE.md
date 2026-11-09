# Tacit: architecture

## Execution

User goal and scoped authorization -> real registered-expert reads -> checked
source evidence -> parent domain reasoning -> human review -> approved workflow
write -> independent readback. No custom NAS runtime or web backend is bundled.
The parent uses standard delegate calls; experts own their CLI options.

## Official capability boundary

The supplied UGOS Skill Creation Tool 0.7.3 and catalog 2.0.0 establish the exact
published CLI/agent ownership and actions in capability-map.md. The controlled
checker is run on the source and extracted ZIP. Its static pass does not verify
permissions, model routing, formats, extraction accuracy or runtime stability.

Free-form document evidence uses qa rather than invented extract schemas.
save-text uses an approved output directory and filename hint; actual outputFile
and verification fields establish the result. No create-only flag is invented.
The no-replacement policy must be enforced by the registered child workflow.
Unsupported guarantees stop an optional write without discarding the preview.

## States and persistence

Collect -> discover -> read -> derive -> review -> approve -> write -> verify.
Empty, unknown or failed required data stops dependents. Partial coverage stays
visible. Changed input or decisions invalidate approval. Unknown write completion
requires inspection before a user-requested retry.

Sources remain unchanged in authorized storage. Reports use only a new approved
location. Prior reports require explicit selection; there is no implicit database,
background watcher or scheduled task.

## Presentation and authoring tests

HTML pages simulate user interactions. Synthetic fixture records and policy-model
tests run outside Uliya. Structural and PDF checks are local development evidence.
The real official checker supplies separate static reports; only the assigned NAS
can establish installation, actual expert behavior and model/data routing.
