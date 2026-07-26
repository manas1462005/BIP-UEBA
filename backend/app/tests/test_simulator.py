import unittest
import httpx
from app.main import app


class TestSimulatorEngine(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = httpx.ASGITransport(app=app)
        self.client = httpx.AsyncClient(transport=self.transport, base_url="http://test")

    async def asyncTearDown(self):
        await self.client.aclose()

    async def test_simulator_generate_endpoint(self):
        response = await self.client.post("/api/v1/simulator/generate?days=1&inject_attacks=true")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertGreater(data["events_count"], 0)

    async def test_simulator_status_endpoint(self):
        response = await self.client.get("/api/v1/simulator/status")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("total_employees", data)
        self.assertIn("total_devices", data)

    async def test_simulator_export_json(self):
        response = await self.client.get("/api/v1/simulator/export?format=json&days=1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("application/json", response.headers["content-type"])

    async def test_simulator_export_csv(self):
        response = await self.client.get("/api/v1/simulator/export?format=csv&days=1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/csv", response.headers["content-type"])


if __name__ == "__main__":
    unittest.main()
