import unittest
import httpx
from app.main import app
from app.ai.anomaly.detector_registry import DetectorRegistry
from app.ai.anomaly.statistical_detector import StatisticalDetector
from app.ai.anomaly.isolation_forest_detector import IsolationForestDetector
from app.ai.anomaly.peer_group_detector import PeerGroupDetector
from app.ai.anomaly.drift_detector import BehaviourDriftDetector
from app.ai.anomaly.sequence_detector import SequenceBehaviourDetector
from app.ai.anomaly.score_fusion import ScoreFusionEngine
from app.ai.anomaly.hybrid_engine import HybridEngine


class TestAnomalyIntelligenceEngine(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = httpx.ASGITransport(app=app)
        self.client = httpx.AsyncClient(transport=self.transport, base_url="http://test")

    async def asyncTearDown(self):
        await self.client.aclose()

    def test_detector_registry(self):
        reg = DetectorRegistry()
        detectors = reg.get_all_detectors()
        self.assertIn("StatisticalDetector", detectors)
        self.assertIn("IsolationForestDetector", detectors)
        self.assertIn("PeerGroupDetector", detectors)
        self.assertIn("BehaviourDriftDetector", detectors)
        self.assertIn("SequenceBehaviourDetector", detectors)

    def test_statistical_detector(self):
        det = StatisticalDetector()
        score1 = det.score({"login_hour": 9}, {"baseline": {"typical_login_hours": [8, 9, 10]}})
        self.assertLessEqual(score1, 0.20)
        score2 = det.score({"login_hour": 3}, {"baseline": {"typical_login_hours": [8, 9, 10]}})
        self.assertGreater(score2, 0.40)

    def test_isolation_forest_detector(self):
        det = IsolationForestDetector()
        score = det.score({"login_hour": 9, "session_duration_minutes": 480}, {})
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_peer_group_detector(self):
        det = PeerGroupDetector()
        score = det.score({"login_hour": 9}, {"peer_group_baseline": {"peer_typical_login_hours": [8, 9, 10]}})
        self.assertLessEqual(score, 0.10)

    def test_drift_detector(self):
        det = BehaviourDriftDetector()
        score = det.score({"threat_label": "Credential Stuffing"}, {"maturity_state": "Stable"})
        self.assertGreater(score, 0.50)

    def test_sequence_detector(self):
        det = SequenceBehaviourDetector()
        score = det.score({"resource_accessed": "Database Cluster"}, {})
        self.assertGreater(score, 0.50)

    def test_score_fusion_engine(self):
        scores = {
            "StatisticalDetector": 0.80,
            "IsolationForestDetector": 0.70,
            "PeerGroupDetector": 0.60,
            "BehaviourDriftDetector": 0.50,
            "SequenceBehaviourDetector": 0.40
        }
        fused = ScoreFusionEngine.fuse_scores(scores)
        self.assertGreaterEqual(fused["hybrid_anomaly_score"], 0.5)
        self.assertIn("StatisticalDetector", fused["detector_contributions"])

    def test_hybrid_engine_evaluation(self):
        eng = HybridEngine()
        res = eng.evaluate_event({"login_hour": 9}, {})
        self.assertIn("hybrid_anomaly_score", res)
        self.assertIn("processing_time_ms", res)

    async def test_score_event_api(self):
        response = await self.client.post("/api/v1/anomaly/score", json={"login_hour": 3, "entity_id": "alex.smith1@bip.com"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("hybrid_anomaly_score", data)

    async def test_get_detectors_api(self):
        response = await self.client.get("/api/v1/anomaly/detectors")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data["detectors"]), 0)

    async def test_get_models_api(self):
        response = await self.client.get("/api/v1/anomaly/models")
        self.assertEqual(response.status_code, 200)

    async def test_train_anomaly_models_api(self):
        response = await self.client.post("/api/v1/anomaly/train", json=[])
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
