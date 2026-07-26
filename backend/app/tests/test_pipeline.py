import unittest
import httpx
from app.main import app
from app.pipeline.event_pipeline import EventPipeline
from app.pipeline.pipeline_queue import PipelineQueue
from app.pipeline.pipeline_manager import PipelineManager
from app.pipeline.pipeline_repository import PipelineRepository


class TestEventPipeline(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = httpx.ASGITransport(app=app)
        self.client = httpx.AsyncClient(transport=self.transport, base_url="http://test")

    async def asyncTearDown(self):
        await self.client.aclose()

    def test_pipeline_queue(self):
        PipelineQueue.enqueue({"event_id": "evt_test_1", "entity_id": "test.user@bip.com"})
        self.assertFalse(PipelineQueue.is_empty())
        item = PipelineQueue.dequeue()
        self.assertEqual(item["event_id"], "evt_test_1")

    async def test_pipeline_status_api(self):
        response = await self.client.get("/api/v1/pipeline/status")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("pipeline_status", data)

    async def test_pipeline_process_api(self):
        sample_event = {
            "event_id": "evt_test_pipeline_001",
            "entity_id": "alex.smith1@bip.com",
            "login_hour": 3,
            "session_duration_minutes": 15,
            "resource_accessed": "AWS Production Console",
            "vpn_used": False,
            "mfa_verified": False,
            "threat_label": "Credential Stuffing"
        }
        response = await self.client.post("/api/v1/pipeline/process", json=sample_event)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["event_id"], "evt_test_pipeline_001")
        self.assertIn("hybrid_anomaly_score", data)
        self.assertIn("context_assessment", data)
        self.assertIn("primary_threat_category", data)
        self.assertIn("explanation_report", data)


if __name__ == "__main__":
    unittest.main()
