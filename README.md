# UGREEN AI NAS Skills Lab

Four developed alternatives, one per hackathon track, plus four archived concepts.
The user-facing HTML demos explain each idea using fictional, hardcoded interactions.

**Release 0.2.0: authored with the official toolkit; all four Skills pass its static checker with zero diagnostics.**
The user supplied UGOS Skill Creation Tool 0.7.3. Its instructions, development
standard and catalog 2.0.0 were used to reconcile expert delegation and supported
actions. Both each source folder and an independent extraction of each ZIP pass.
See [official evidence](validation/official/README.md). Installation and execution
on the assigned NAS remain untested.

[Open the demo collection](index.html) · [Leer en español](README.es.md) · [Delivery status](STATUS.md)

## Selected alternatives

| Track | Product | Purpose | Materials |
| --- | --- | --- | --- |
| Automate Your Workflow | [Tacit](products/tacit/README.md) | Preserve practical knowledge as a source-linked procedure, question queue and teach-back exercise. | [Demo](products/tacit/demo.html) · [PDF](deliverables/tacit/v0.2.0/tacit-proposal.pdf) · [Skill ZIP](deliverables/tacit/v0.2.0/tacit-initial-skill.zip) |
| Bring Memories to Life | [Off Camera](products/off-camera/README.md) | Prepare an explicitly reviewed photo selection representing chosen people. | [Demo](products/off-camera/demo.html) · [PDF](deliverables/off-camera/v0.2.0/off-camera-proposal.pdf) · [Skill ZIP](deliverables/off-camera/v0.2.0/off-camera-initial-skill.zip) |
| Unleash Your Creativity | [ContextCut](products/contextcut/README.md) | Review lost qualifications, negations and attribution while shortening interviews. | [Demo](products/contextcut/demo.html) · [PDF](deliverables/contextcut/v0.2.0/contextcut-proposal.pdf) · [Skill ZIP](deliverables/contextcut/v0.2.0/contextcut-initial-skill.zip) |
| Open Innovation | [BenchMatch](products/benchmatch/README.md) | Compare two prototype runs without hiding unknowns or claiming causality. | [Demo](products/benchmatch/demo.html) · [PDF](deliverables/benchmatch/v0.2.0/benchmatch-proposal.pdf) · [Skill ZIP](deliverables/benchmatch/v0.2.0/benchmatch-initial-skill.zip) |

Each selected product contains a complete authored workflow, six directly linked
Markdown references, an English ten-answer proposal, synthetic fixtures, a user
guide, an architecture note, finalist validation cases and a demonstration outline.
The ZIPs contain only the named Skill directory, SKILL.md and references/*.md.
Development Python, HTML, PDFs, fixtures and repository metadata are outside them.
Older, unversioned artifacts are preserved as the provisional baseline; use the
versioned release linked above for review and selection.

## Archived concepts

| Concept | Explanation | Demo |
| --- | --- | --- |
| LotTrace | [Trace a material lot to orders](concepts/lottrace/README.md) | [Try](concepts/lottrace/demo.html) |
| Date Detective | [Constrain an old photo's date with evidence](concepts/date-detective/README.md) | [Try](concepts/date-detective/demo.html) |
| Continuity Desk | [Review scene continuity](concepts/continuity-desk/README.md) | [Try](concepts/continuity-desk/demo.html) |
| ShareScope | [Review an audience-specific sharing selection](concepts/sharescope/README.md) | [Try](concepts/sharescope/demo.html) |

Each archived concept intentionally contains just its original demo and README.
It has no Skill package or proposal PDF.

## Try the demos

Open index.html with a browser, or any product's demo.html directly. No server,
installation or Internet connection is required. Each page includes its styles,
JavaScript, synthetic records and licensed font. Choose the main, incomplete or
empty case; inspect sources; authorize the example; make a decision; review and
approve a simulated save; download a real example report through the browser.

Changing a prepared request does not invoke a model. There is no backend, upload,
NAS connection, live transcription, real photo recognition or real album creation.
The photo views are illustrative records, not photographs.

## What actually runs on NAS

The intended product is a Markdown Uliya Skill. It coordinates registered experts;
the parent reasons about returned evidence. A separate web application is not
required or bundled as a NAS runtime. CLI/action/agent bindings now match the
supplied official catalog. Free-form document extraction uses the document
expert's qa capability. Report saving follows save-text's directory and actual
returned outputFile contract. Exact album creation remains conditional on the
photo expert establishing item binding and complete membership readback.

The HTML collection and development policy models are separate presentation and
authoring aids. They cannot prove NAS compatibility, model accuracy, locality,
permissions, exact album membership semantics or reliable installation.

## Reproduce local checks

Rebuilding requires Python 3.10+, Node.js and a separate copy of the official
toolkit. PDF text validation additionally uses pypdf. The toolkit is not
redistributed here. Pass the path to its extracted uliya-skill-kit directory:

~~~sh
python3 tools/build_candidates.py --kit /path/to/uliya-skill-kit
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
~~~

The builder invokes the actual official checker before promoting immutable,
versioned ZIP/PDF artifacts. A changed artifact requires a new release version.
[validation/local-checks.json](validation/local-checks.json) separately verifies
structure, PDF content and the official reports' per-file hashes. The generic
Codex metadata checker is an additional check. [validation/REVIEW.md](validation/REVIEW.md)
records independent paper walkthroughs and their limited scope.

## Entering the hackathon

The [official rules](https://ugreenhackathon.devpost.com/rules) allow only **one
project per entrant or team**. These are alternatives for selection, not four
separate permitted entries. Choose one, review all generated claims and
disclosures, and submit its versioned PDF plus Skill ZIP.

Round 1 requires no NAS evidence or demo video. A Round 2 entry must remain the
same project and needs actual assigned-NAS operation and a public English demo.
Do not upload the repository archive or browser demo as the Skill package.

## Rights, data and publication

No project-wide open-source license has been assigned to original project content.
Third-party rights remain unchanged; see [THIRD_PARTY.md](THIRD_PARTY.md).
All bundled source fixtures are fictional. No entrant identity, signature, consent
declaration or Devpost submission has been invented or made on the user's behalf.

Remote publication is separate from local preparation. The intended destination
is a new private GitHub repository; [PUBLISHING.md](PUBLISHING.md) states the exact
steps and the network blocker. The user reports authentication completed; this
session cannot resolve GitHub hosts to verify it. No upload is claimed without
a returned repository URL and verified remote commit.
