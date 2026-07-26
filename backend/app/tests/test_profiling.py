import unittest
import httpx
from app.main import app
from app.ai.profiling.feature_extractor import FeatureExtractor
from app.ai.profiling.confidence_engine import ConfidenceEngine
from app.ai.profiling.maturity_engine import MaturityEngine
from app.ai.profiling.profile_builder import ProfileBuilder
from app.ai.profiling.version_manager import VersionManager


class TestProfilingEngine(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = httpx.ASGITransport(app=app)
        self.client = httpx.AsyncClient(transport=self.transport, base_url="http://test")

    async def asyncTearDown(self):
        await self.client.aclose()

    def test_feature_extraction(self):
        sample_event = {
            "timestamp": "2026-07-25T14:30:00Z",
            "entity_id": "alex.smith1@bip.com",
            "source_ip": "10.100.4.12",
            "device_id": "dev_1001",
            "resource_accessed": "AWS Console",
            "vpn_used": False
        }
        features = FeatureExtractor.extract_features(sample_event)
        self.assertEqual(features["entity_id"], "alex.smith1@bip.com")
        self.assertEqual(features["login_hour"], 14)
        self.assertEqual(features["resource_sensitivity"], "Critical")

    def test_confidence_engine(self):
        features = [{"source_ip": "10.100.4.12"} for _ in range(30)]
        conf = ConfidenceEngine.calculate_confidence(features)
        self.assertGreaterEqual(conf["confidence_score"], 0.5)

    def test_maturity_engine(self):
        mat1 = MaturityEngine.determine_maturity(3, 0.4)
        self.assertEqual(mat1, "New")
        mat2 = MaturityEngine.determine_maturity(60, 0.9)
        self.assertEqual(mat2, "Trusted")

    def test_profile_builder(self):
        raw_events = [{"timestamp": "2026-07-25T09:00:00Z", "entity_id": "user@bip.com"}]
        prof = ProfileBuilder.build_profile("user@bip.com", "user", raw_events)
        self.assertEqual(prof["entity_id"], "user@bip.com")
        self.assertIn("behavior_fingerprint", prof)

    def test_version_manager(self):
        prof = {"entity_id": "user@bip.com", "version": 1}
        snap = VersionManager.create_version_snapshot(prof, previous_version=1)
        self.assertEqual(snap["version"], 2)

    async def test_get_user_profile_api(self):
        response = await self.client.get("/api/v1/profiles/users/user@bip.com")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["entity_id"], "user@bip.com")

    async def test_get_device_profile_api(self):
        response = await self.client.get("/api/v1/profiles/devices/dev_1001")
        self.assertEqual(response.status_code, 200)

    async def test_get_team_profile_api(self):
        response = await self.client.get("/api/v1/profiles/teams/TEAM-ENG-01")
        self.assertEqual(response.status_code, 200)

    async def test_get_enterprise_profile_api(self):
        response = await self.client.get("/api/v1/profiles/enterprise")
        self.assertEqual(response.status_code, 200)

    async def test_rebuild_profiles_api(self):
        response = await self.client.post("/api/v1/profiles/rebuild")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "rebuilt")


if __name__ == "__main__":
    unittest.main()
