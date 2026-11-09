# Off Camera selection contract

## Identity and scope

An asset key includes its returned identifier type and value. A filesystem path,
photo-library asset ID and people ID are different types and cannot be substituted.
Use confirmed people labels only. Treat unrecognized or uncertain people as
unknown. If confirmed identities are unavailable, the user may manually identify
the candidate assets; keep that provenance.

## Bounded deterministic heuristic

Maintain counts for the chosen priority people. First address an uncovered person
with the fewest candidate photos, breaking ties by the user's priority order.
Among that person's candidates, prefer the one covering most still-uncovered
priority people, then a distinct known event, then the lexicographically smallest
actual asset key. Continue until coverage is exhausted or the requested size is
reached. For each remaining fill slot, find the smallest selected-appearance
count among all priority people, including uncovered people with zero appearances.
Score a candidate by the number of its confirmed priority people currently at
that minimum. Prefer the highest score, then a distinct known event, then the
lexicographically smallest typed asset key (identifier type, identifier value).
Recompute counts after each choice. If a zero-match person makes all scores zero,
the event/key ties still determine the next choice; the coverage gap remains.

This is a reviewable greedy heuristic, not a global optimization claim. A repeated
candidate may be selected only once. The resulting count must equal the requested
count or an explicitly agreed reduced count. If there are fewer distinct assets,
ask before changing the goal; do not pad the album or ignore the size.

## Coverage

For each priority person show selected confirmed appearances, available candidate
count and uncertainty. Zero means no confirmed match in the checked scope, not
absence from the event. Unknown event labels earn no diversity preference.
Capture date and import date must remain distinct. If timing is unknown, ask
whether to include that asset; do not silently interpret import time as capture.

## Review and album guard

Any membership or priority change invalidates prior approval. The exact final set
is the report's canonical selection. Album creation is conditional on supported
exact-set semantics and separately approved. Require identical typed member sets
on readback; a similar count or matching title alone does not verify membership.
If the report saves but the album fails, report the two outcomes separately.
