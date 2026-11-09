"""Development-only policy examples, never a NAS runtime or Skill executor."""
from collections import Counter
from decimal import Decimal, InvalidOperation
import hashlib
import json


def procedure_state(claims, *, actor_known=True, condition_known=True):
    """Preserve incompatible instructions within the same declared context."""
    groups = {}
    for claim in claims:
        if not claim.get("source") or not claim.get("readable", True):
            continue
        key = (claim["action"], claim.get("condition"), claim.get("version"))
        groups.setdefault(key, set()).add(claim["instruction"])
    if any(len(values) > 1 for values in groups.values()):
        return "CONFLICTING"
    if not groups:
        return "UNREADABLE"
    if not actor_known or not condition_known:
        return "NEEDS_CLARIFICATION"
    return "SUPPORTED"


def teachback_eligible(state):
    return state == "SUPPORTED"


def classify_quote(draft, original, *, source=None, attribution_confirmed=False):
    """Conservative grounding guard; semantic findings require editorial evidence."""
    if not source or not original or not attribution_confirmed:
        return "UNVERIFIED"
    if " ".join(draft.split()) == " ".join(original.split()):
        return "EXACT"
    return "MANUAL_REVIEW"


def supported_alternative(original, alternative):
    """Only a contiguous nonempty source excerpt passes this narrow helper."""
    return bool(alternative.strip()) and alternative in original


def record_quote_decision(evidence_status, decision):
    allowed = {"ACCEPT_ALTERNATIVE", "RETAIN_WITH_NOTE", "UNRESOLVED"}
    if decision not in allowed:
        raise ValueError("Unrecognized editor decision")
    return {"evidence_status": evidence_status, "editor_decision": decision}


def asset_key(candidate):
    if not candidate.get("id") or not candidate.get("type"):
        raise ValueError("A typed, actual candidate identity is required")
    return candidate["type"], candidate["id"]


def select_photos(candidates, priorities, requested, *, reduced_count_agreed=False):
    if len(candidates) > 60 or not 2 <= len(priorities) <= 8:
        raise ValueError("Outside the bounded selection contract")
    if len(set(priorities)) != len(priorities):
        raise ValueError("Priority people must be unique")
    if not isinstance(requested, int) or isinstance(requested, bool):
        raise ValueError("Count must be an integer")
    if requested < 1 or requested > 12 or (requested < 4 and not reduced_count_agreed):
        raise ValueError("Count requires explicit agreement")
    unique = {}
    for candidate in candidates:
        key = asset_key(candidate)
        if key in unique and unique[key] != candidate:
            raise ValueError("Conflicting metadata for one identity")
        unique[key] = candidate
    remaining = dict(unique)
    if len(remaining) < requested:
        raise ValueError("Insufficient candidates; obtain an agreed reduced count")
    selected, counts, events = [], Counter(), set()
    priority_set = set(priorities)
    while len(selected) < requested:
        uncovered = [p for p in priorities if counts[p] == 0]
        coverable = [
            p for p in uncovered
            if any(p in c.get("people", []) for c in remaining.values())
        ]
        if coverable:
            person = min(
                coverable,
                key=lambda p: (
                    sum(p in c.get("people", []) for c in remaining.values()),
                    priorities.index(p),
                ),
            )
            options = [c for c in remaining.values() if person in c.get("people", [])]
            def rank(c):
                people = set(c.get("people", [])) & priority_set
                event = c.get("event")
                return (-len(people & set(uncovered)),
                        -int(bool(event) and event not in events), asset_key(c))
        else:
            options = list(remaining.values())
            minimum = min(counts[p] for p in priorities)
            def rank(c):
                people = set(c.get("people", [])) & priority_set
                event = c.get("event")
                return (-sum(counts[p] == minimum for p in people),
                        -int(bool(event) and event not in events), asset_key(c))
        chosen = min(options, key=rank)
        selected.append(chosen)
        del remaining[asset_key(chosen)]
        counts.update(set(chosen.get("people", [])) & priority_set)
        if chosen.get("event"):
            events.add(chosen["event"])
    return {
        "selected": selected,
        "coverage": {p: counts[p] for p in priorities},
        "unrepresented": [p for p in priorities if counts[p] == 0],
    }


def verify_album(approved, actual):
    try:
        expected_keys = [asset_key(c) for c in approved]
        actual_keys = [asset_key(c) for c in actual]
    except ValueError:
        return False
    return (len(expected_keys) == len(set(expected_keys))
            and len(actual_keys) == len(set(actual_keys))
            and set(expected_keys) == set(actual_keys))


def compare_observations(a, b, *, tolerance=None):
    def readable(items):
        return [i for i in items if i.get("readable", True) and i.get("value") is not None]
    left, right = readable(a), readable(b)
    # A conflict can be known even when the opposite run is missing.
    for values in (left, right):
        by_unit = {}
        for item in values:
            by_unit.setdefault(item.get("unit"), set()).add(str(item["value"]))
        if any(len(v) > 1 for v in by_unit.values()):
            return "CONFLICTING"
    if not left or not right:
        return "UNKNOWN"
    if len({i.get("unit") for i in left + right}) != 1 or not left[0].get("unit"):
        return "NOT_COMPARABLE"
    x, y = left[0]["value"], right[0]["value"]
    if tolerance is not None:
        try:
            threshold = Decimal(str(tolerance))
            dx, dy = Decimal(str(x)), Decimal(str(y))
        except InvalidOperation as error:
            raise ValueError("A numeric tolerance requires numeric observations") from error
        if not all(v.is_finite() for v in (threshold, dx, dy)) or threshold < 0:
            raise ValueError("Tolerance and observations must be finite; tolerance nonnegative")
        return "MATCH" if abs(dx-dy) <= threshold else "DIFFERENT"
    return "MATCH" if str(x) == str(y) else "DIFFERENT"


class Approval:
    """Demonstrate approval invalidation against a complete reviewed snapshot."""
    def __init__(self):
        self.approved = None

    @staticmethod
    def fingerprint(snapshot):
        return hashlib.sha256(json.dumps(snapshot, sort_keys=True).encode()).hexdigest()

    def approve(self, snapshot):
        self.approved = self.fingerprint(snapshot)

    def permits(self, snapshot):
        return self.approved is not None and self.approved == self.fingerprint(snapshot)
