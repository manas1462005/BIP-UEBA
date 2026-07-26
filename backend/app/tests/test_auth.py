import unittest
import httpx
from app.main import app


class TestAuthEndpoints(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = httpx.ASGITransport(app=app)
        self.client = httpx.AsyncClient(transport=self.transport, base_url="http://test")

    async def asyncTearDown(self):
        await self.client.aclose()

    async def test_mock_login_admin_success(self):
        response = await self.client.post(
            "/api/v1/auth/login",
            json={"username": "admin@bip.com", "password": "Admin123!"}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("access_token", data)
        self.assertEqual(data["token_type"], "bearer")
        self.assertEqual(data["role"], "Admin")

    async def test_mock_login_analyst_success(self):
        response = await self.client.post(
            "/api/v1/auth/login",
            json={"username": "analyst@bip.com", "password": "Analyst123!"}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["role"], "Analyst")

    async def test_mock_login_invalid_password(self):
        response = await self.client.post(
            "/api/v1/auth/login",
            json={"username": "admin@bip.com", "password": "WrongPassword!"}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["detail"], "Incorrect email or password")


if __name__ == "__main__":
    unittest.main()
