"""Observable invariants of development policy models, not NAS behavior."""
from pathlib import Path
import json
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from reference_models import (
    Approval, classify_quote, compare_observations, procedure_state,
    record_quote_decision, select_photos, supported_alternative,
    teachback_eligible, verify_album,
)


class TacitPolicy(unittest.TestCase):
    def claim(self, instruction, version="v2", **extra):
        return dict(action="release", condition="over budget", version=version,
                    instruction=instruction, source="procedure.md", **extra)

    def test_unsupported_procedure_is_not_invented(self):
        self.assertEqual(procedure_state([]), "UNREADABLE")

    def test_missing_actor_stays_open(self):
        self.assertEqual(procedure_state([self.claim("ask supervisor")],
                                         actor_known=False), "NEEDS_CLARIFICATION")

    def test_conflict_prevents_settled_teaching(self):
        state=procedure_state([self.claim("ask supervisor"),self.claim("ship now")])
        self.assertEqual(state,"CONFLICTING")
        self.assertFalse(teachback_eligible(state))

    def test_different_versions_are_not_silently_merged(self):
        self.assertEqual(procedure_state([
            self.claim("ask supervisor","v2"),self.claim("ship now","v1")
        ]),"SUPPORTED")

    def test_unreadable_claim_does_not_support_answer(self):
        self.assertEqual(procedure_state([self.claim("ship now",readable=False)]),
                         "UNREADABLE")

    def test_supported_step_can_be_taught(self):
        self.assertTrue(teachback_eligible(procedure_state([self.claim("ask supervisor")])))


class ContextCutPolicy(unittest.TestCase):
    def test_exact_source_and_attribution_required(self):
        self.assertEqual(classify_quote("We started in 2018.","We started in 2018.",
            source="ana.md",attribution_confirmed=True),"EXACT")

    def test_missing_source_stays_unverified(self):
        self.assertEqual(classify_quote("A","A",attribution_confirmed=True),"UNVERIFIED")

    def test_attribution_cannot_be_guessed(self):
        self.assertEqual(classify_quote("A","A",source="anonymous.md"),"UNVERIFIED")

    def test_changed_negation_is_not_exact(self):
        self.assertEqual(classify_quote("We recommend it.","We do not recommend it.",
            source="leo.md",attribution_confirmed=True),"MANUAL_REVIEW")

    def test_retaining_cut_does_not_verify_source(self):
        result=record_quote_decision("UNVERIFIED","RETAIN_WITH_NOTE")
        self.assertEqual(result["evidence_status"],"UNVERIFIED")

    def test_contiguous_alternative_supported(self):
        self.assertTrue(supported_alternative(
            "We will stop using plastic in the cafe; shipping is excluded.",
            "We will stop using plastic in the cafe"))

    def test_spliced_alternative_is_not_verbatim(self):
        self.assertFalse(supported_alternative(
            "We do not recommend it, but another person does.","We recommend it"))

    def test_empty_alternative_rejected(self):
        self.assertFalse(supported_alternative("A",""))


class OffCameraPolicy(unittest.TestCase):
    def setUp(self):
        self.photos=json.loads((ROOT/"products/off-camera/fixtures/candidate-photos.json").read_text())
        self.people=["Ana","Diego","Lucia","Sofia"]

    def test_four_distinct_real_assets_cover_photographer(self):
        result=select_photos(self.photos,self.people,4)
        self.assertEqual(len({p["id"] for p in result["selected"]}),4)
        self.assertGreater(result["coverage"]["Ana"],0)
        self.assertTrue(all(p in self.photos for p in result["selected"]))

    def test_repeated_calls_have_stable_selection(self):
        self.assertEqual(select_photos(self.photos,self.people,4),
                         select_photos(list(reversed(self.photos)),self.people,4))

    def test_no_match_is_retained_as_gap(self):
        result=select_photos(self.photos[:4],self.people,4)
        self.assertIn("Ana",result["unrepresented"])
        self.assertEqual(result["coverage"]["Ana"],0)

    def test_no_automatic_count_reduction(self):
        with self.assertRaises(ValueError):
            select_photos(self.photos[:3],self.people,4)

    def test_explicit_reduced_count(self):
        self.assertEqual(len(select_photos(self.photos[:3],self.people,3,
                         reduced_count_agreed=True)["selected"]),3)

    def test_duplicate_assets_are_not_extra_photos(self):
        result=select_photos(self.photos+[self.photos[0]],self.people,4)
        self.assertEqual(len({p["id"] for p in result["selected"]}),4)

    def test_conflicting_identity_metadata_stops(self):
        conflict={**self.photos[0],"people":["Ana"]}
        with self.assertRaises(ValueError):
            select_photos(self.photos+[conflict],self.people,4)

    def test_type_is_part_of_identity(self):
        approved=self.photos[:4]
        actual=[{**p,"type":"filesystem-path"} for p in approved]
        self.assertFalse(verify_album(approved,actual))

    def test_album_count_is_insufficient(self):
        self.assertFalse(verify_album(self.photos[:4],self.photos[1:5]))

    def test_exact_set_verifies(self):
        self.assertTrue(verify_album(self.photos[:4],list(reversed(self.photos[:4]))))

    def test_duplicate_members_fail_verification(self):
        self.assertFalse(verify_album(self.photos[:4],self.photos[:4]+[self.photos[0]]))

    def test_large_scope_requires_narrowing(self):
        with self.assertRaises(ValueError):
            select_photos(self.photos*8,self.people,4)


class BenchMatchPolicy(unittest.TestCase):
    def value(self,value,unit="C",**extra):
        return dict(value=value,unit=unit,**extra)

    def test_explicit_numeric_difference(self):
        self.assertEqual(compare_observations([self.value(200)],[self.value(215)]),
                         "DIFFERENT")

    def test_agreeing_values_match(self):
        self.assertEqual(compare_observations([self.value(55,"mm/s")],
                                             [self.value(55,"mm/s")]),"MATCH")

    def test_unknown_does_not_become_zero(self):
        self.assertEqual(compare_observations([self.value(44,"%")],[]),"UNKNOWN")

    def test_unreadable_value_is_not_evidence(self):
        self.assertEqual(compare_observations([self.value(200)],
            [self.value(215,readable=False)]),"UNKNOWN")

    def test_run_conflict_is_not_averaged(self):
        self.assertEqual(compare_observations([self.value(200)],
            [self.value(215),self.value(205)]),"CONFLICTING")

    def test_unit_mapping_not_invented(self):
        self.assertEqual(compare_observations([self.value(200)],
            [self.value(392,"F")]),"NOT_COMPARABLE")

    def test_declared_tolerance(self):
        self.assertEqual(compare_observations([self.value(200)],
            [self.value(201)],tolerance=1),"MATCH")

    def test_negative_tolerance_rejected(self):
        with self.assertRaises(ValueError):
            compare_observations([self.value(200)],[self.value(201)],tolerance=-1)

    def test_nonfinite_tolerance_rejected(self):
        with self.assertRaises(ValueError):
            compare_observations([self.value(200)],[self.value(201)],tolerance="NaN")


class ApprovalPolicy(unittest.TestCase):
    def test_write_has_no_default_approval(self):
        self.assertFalse(Approval().permits({"report":"draft"}))

    def test_same_review_snapshot_can_be_approved(self):
        gate=Approval();value={"report":"reviewed","sources":["a"]}
        gate.approve(value);self.assertTrue(gate.permits(value))

    def test_membership_change_invalidates_approval(self):
        gate=Approval();gate.approve({"ids":["F01","F02","F03","F04"]})
        self.assertFalse(gate.permits({"ids":["F01","F02","F03"]}))

    def test_source_change_invalidates_approval(self):
        gate=Approval();gate.approve({"source_identity":"version A"})
        self.assertFalse(gate.permits({"source_identity":"version B"}))

    def test_new_user_decision_requires_new_review(self):
        gate=Approval();gate.approve({"decision":"UNRESOLVED"})
        self.assertFalse(gate.permits({"decision":"ACCEPT_ALTERNATIVE"}))


if __name__ == "__main__":
    unittest.main()
