import unittest
import httpx
from app.main import app


class TestEnterpriseContextEngine(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = httpx.ASGITransport(app=app)
        self.client = httpx.AsyncClient(transport=self.transport, base_url="http://test")

    async def asyncTearDown(self):
        await self.client.aclose()

    async def test_get_enterprise_metadata(self):
        response = await self.client.get("/api/v1/enterprise")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["organization"], "Global CyberTech Enterprise")
        self.assertIn("business_units", data)

    async def test_get_projects_api(self):
        response = await self.client.get("/api/v1/projects")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data["projects"]), 0)

    async def test_get_teams_api(self):
        response = await self.client.get("/api/v1/teams")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data["teams"]), 0)

    async def test_get_network_topology_api(self):
        response = await self.client.get("/api/v1/network")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data["topology"]), 0)

    async def test_get_policies_api(self):
        response = await self.client.get("/api/v1/policies")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data["policies"]), 0)

    async def test_get_employee_relationships_api(self):
        response = await self.client.get("/api/v1/relationships/EMP-1001")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["employee_id"], "EMP-1001")
        self.assertGreater(len(data["relationships"]), 0)

    async def test_get_calendar_api(self):
        response = await self.client.get("/api/v1/calendar")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data["calendar_events"]), 0)


if __name__ == "__main__":
    unittest.main()
