import unittest
import httpx
from app.main import app
from app.ai.threat.threat_classifier import ThreatClassifier, TAXONOMY_CATEGORIES
from app.ai.threat.hypothesis_engine import ThreatHypothesisEngine
from app.simulator.attack_campaign_generator import AttackCampaignGenerator
from app.ai.explainability.report_generator import ReportGenerator
from app.database.session import SessionLocal


class TestAssignmentCompliance(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = httpx.ASGITransport(app=app)
        self.client = httpx.AsyncClient(transport=self.transport, base_url="http://test")
        self.db = SessionLocal()

    async def asyncTearDown(self):
        await self.client.aclose()
        self.db.close()

    def test_taxonomy_categories_coverage(self):
        self.assertEqual(len(TAXONOMY_CATEGORIES), 8)
        required_8 = [
            "Normal Baseline", "Brute Force", "Impossible Travel",
            "Credential Stuffing", "Lateral Movement", "Device Spoofing",
            "Low-and-Slow Exfiltration", "Insider Drift"
        ]
        for cat in required_8:
            self.assertIn(cat, TAXONOMY_CATEGORIES)

    def test_threat_classifier_assignment_taxonomy(self):
        hypotheses = [{"hypothesis_name": "Brute Force Password Spray", "probability": 0.90, "confidence": 0.95}]
        res = ThreatClassifier.classify_threat({}, hypotheses)
        self.assertEqual(res["primary_threat_category"], "Brute Force")

        hypotheses_it = [{"hypothesis_name": "Impossible Travel Anomaly", "probability": 0.90, "confidence": 0.95}]
        res_it = ThreatClassifier.classify_threat({}, hypotheses_it)
        self.assertEqual(res_it["primary_threat_category"], "Impossible Travel")

    def test_synthetic_data_generator_fields(self):
        emp = {"user_id": "usr_001", "email": "test@bip.com", "department": "Engineering"}
        dev = {"device_id": "dev_001", "fingerprint": "fp_corp"}
        events = AttackCampaignGenerator.inject_attack_campaign(emp, dev, [], None, specific_scenario="Brute Force")
        self.assertTrue(len(events) > 0)
        evt = events[0]

        required_fields = [
            "entity_id", "entity_type", "timestamp", "source_ip",
            "geo_location", "resource_accessed", "authentication_method",
            "session_duration", "command_sequence", "device_fingerprint", "threat_label"
        ]
        for field in required_fields:
            self.assertIn(field, evt)

    def test_investigation_report_generator_6_sections(self):
        report_gen = ReportGenerator(self.db)
        report = report_gen.generate_full_investigation_report({
            "entity_id": "alex.smith1@bip.com",
            "event_id": "evt_compliance_001"
        })

        required_sections = [
            "behavioural_assumptions",
            "detected_anomalies",
            "attack_classification",
            "explainability_output",
            "evaluation_metrics",
            "known_limitations"
        ]
        for section in required_sections:
            self.assertIn(section, report)

    async def test_full_report_api_endpoint(self):
        response = await self.client.get("/api/v1/explain/report/full?entity_id=alex.smith1@bip.com")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("behavioural_assumptions", data)
        self.assertIn("detected_anomalies", data)
        self.assertIn("attack_classification", data)
        self.assertIn("explainability_output", data)
        self.assertIn("evaluation_metrics", data)
        self.assertIn("known_limitations", data)


if __name__ == "__main__":
    unittest.main()
