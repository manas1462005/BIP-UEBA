import unittest
import httpx
from app.main import app
from app.ai.threat.evidence_aggregator import EvidenceAggregator
from app.ai.threat.hypothesis_engine import ThreatHypothesisEngine
from app.ai.threat.threat_classifier import ThreatClassifier
from app.ai.threat.mitre_mapper import MITREMapper
from app.ai.threat.attack_chain_builder import AttackChainBuilder
from app.ai.threat.threat_repository import ThreatRepository


class TestThreatIntelligenceEngine(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = httpx.ASGITransport(app=app)
        self.client = httpx.AsyncClient(transport=self.transport, base_url="http://test")

    async def asyncTearDown(self):
        await self.client.aclose()

    def test_evidence_aggregation(self):
        res = EvidenceAggregator.aggregate_evidence(
            {"entity_id": "alex.smith1@bip.com", "threat_label": "Credential Stuffing"},
            {},
            {"hybrid_anomaly_score": 0.85},
            {"context_assessment": "Unjustified High-Risk Deviation"}
        )
        self.assertEqual(res["hybrid_score"], 0.85)
        self.assertEqual(res["threat_label"], "Credential Stuffing")

    def test_hypothesis_generation(self):
        evidence = {"hybrid_score": 0.85, "context_assessment": "Unjustified High-Risk Deviation", "threat_label": "Credential Stuffing"}
        hypotheses = ThreatHypothesisEngine.generate_hypotheses(evidence)
        self.assertGreater(len(hypotheses), 1)
        self.assertIn("Credential Theft", hypotheses[0]["hypothesis_name"])

    def test_threat_classification(self):
        hypotheses = [{"hypothesis_name": "Credential Theft & Password Spray Attack", "probability": 0.65, "confidence": 0.90}]
        res = ThreatClassifier.classify_threat({}, hypotheses)
        self.assertEqual(res["primary_threat_category"], "Credential Stuffing")

    def test_mitre_mapping(self):
        mappings = MITREMapper.map_mitre_attack("Credential Stuffing")
        self.assertGreater(len(mappings), 0)

    def test_attack_chain_builder(self):
        chain = AttackChainBuilder.build_attack_chain("Credential Stuffing", {})
        self.assertGreater(len(chain), 1)

    async def test_classify_threat_api(self):
        response = await self.client.post("/api/v1/threat/classify", json={"entity_id": "alex.smith1@bip.com", "threat_label": "Credential Stuffing"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("primary_classification", data)

    async def test_get_threat_history_api(self):
        response = await self.client.get("/api/v1/threat/history")
        self.assertEqual(response.status_code, 200)
        data = response.json()


if __name__ == "__main__":
    unittest.main()
