# Official capability evidence

Source: UGOS Skill Creation Tool 0.7.3, catalog 2.0.0, supplied by the user.
Catalog SHA-256: c927fd8e233696cd152baf98468368912c13c08aabeac353f0ee95c46c0428e6.
Only published CLI families and their unique agent mappings are used.
Actions below are generation-time evidence; experts own their actual options.

| CLI | Registered expert | Action | Effect | Approval |
| --- | --- | --- | --- | --- |
| `ug-filesystem` | `file-agent` | `find` | read | none |
| `ug-filesystem` | `file-agent` | `stat` | read | none |
| `ug-filesystem` | `file-agent` | `cat` | read | none |
| `ug-filesystem` | `file-agent` | `sha256sum` | read | none |
| `ug-photo` | `photo-agent` | `albums` | read | none |
| `ug-photo` | `photo-agent` | `figure-albums` | read | none |
| `ug-photo` | `photo-agent` | `search-picture` | read | none |
| `ug-photo` | `photo-agent` | `meta` | read | none |
| `ug-photo` | `photo-agent` | `create-album` | state-change | workflow |
| `ug-photo` | `photo-agent` | `album-detail` | read | none |
| `ug-knowledge` | `knowledge-agent` | `save-text` | state-change | workflow |

## What the catalog does not establish

Permissions, prerequisites, error codes, action stability and example result
status are marked unknown. Confirm actual formats, routing, coverage and
approval behavior on the assigned NAS; do not interpret a static pass as
a runtime test.

## Reading documents

The qa action supports content_read, extraction, comparison and
locate_content intents, with actual evidence and coverage returned by the
expert. The separate extract action has a fixed schema list; no custom
procedure, interview or prototype-run schema is asserted.

## Saving

save-text has workflow approval and returns verified, outputFile and
contentBytes. Treat its path as an output-directory choice, not proof that
an arbitrary literal filename was written. Preserve no-replacement policy
through the child workflow and use actual outputFile for readback.

## Exact album membership

create-album exposes repeatable add-item. Its item encoding and exact-set
behavior must be confirmed by photo-agent on the device. The distinct
create-album-custom action exposes only a name; do not use it as a
claimed exact-membership implementation. Check returned album_uuid and
query its members through search-picture; album-detail alone does not
promise complete membership. Unsupported exact-set behavior stops that
optional branch while keeping the reviewed selection report.
