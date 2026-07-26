import unittest
import httpx
from app.main import app
from app.ai.context.trust_reasoning import TrustReasoningEngine
from app.ai.context.relationship_reasoning import RelationshipReasoningEngine
from app.ai.context.calendar_reasoning import CalendarReasoningEngine
from app.ai.context.policy_reasoning import PolicyReasoningEngine
from app.ai.context.business_criticality import BusinessCriticalityEngine
from app.ai.context.context_assessment import ContextAssessmentEngine
from app.ai.context.reasoning_pipeline import ReasoningPipeline


class TestContextIntelligenceEngine(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = httpx.ASGITransport(app=app)
        self.client = httpx.AsyncClient(transport=self.transport, base_url="http://test")

    async def asyncTearDown(self):
        await self.client.aclose()

    def test_trust_reasoning(self):
        res = TrustReasoningEngine.evaluate_trust({"device_id": "dev_laptop_1", "mfa_verified": True, "vpn_used": True}, {})
        self.assertEqual(res["trust_level"], "High Trust")
        self.assertTrue(res["is_managed_device"])

    def test_relationship_reasoning(self):
        res = RelationshipReasoningEngine.evaluate_relationships({"resource_accessed": "Azure Active Directory"}, {})
        self.assertEqual(res["relationship_distance_hops"], 1.0)

    def test_calendar_reasoning(self):
        res = CalendarReasoningEngine.evaluate_calendar({"login_hour": 3, "resource_accessed": "AWS Production Console"}, {})
        self.assertTrue(res["calendar_justified"])

    def test_policy_reasoning(self):
        res = PolicyReasoningEngine.evaluate_policy({"resource_accessed": "AWS Production Console"}, {})
        self.assertTrue(res["is_jit_temporary_access"])

    def test_business_criticality(self):
        res = BusinessCriticalityEngine.evaluate_criticality({"resource_accessed": "AWS Production Console"}, {})
        self.assertEqual(res["resource_sensitivity"], "Critical")

    def test_context_assessment_synthesis(self):
        trust = TrustReasoningEngine.evaluate_trust({"device_id": "dev_1", "mfa_verified": True}, {})
        rel = RelationshipReasoningEngine.evaluate_relationships({"resource_accessed": "Azure Active Directory"}, {})
        cal = CalendarReasoningEngine.evaluate_calendar({"login_hour": 9}, {})
        policy = PolicyReasoningEngine.evaluate_policy({}, {})
        crit = BusinessCriticalityEngine.evaluate_criticality({}, {})

        assessment = ContextAssessmentEngine.synthesize_assessment(0.10, trust, rel, cal, policy, crit)
        self.assertIn("context_assessment", assessment)
        self.assertGreater(len(assessment["reasoning_trace"]), 0)

    def test_reasoning_pipeline(self):
        res = ReasoningPipeline.execute({"entity_id": "alex.smith1@bip.com"}, {}, 0.20)
        self.assertIn("reasoning_trace", res)

    async def test_evaluate_context_api(self):
        response = await self.client.post("/api/v1/context/evaluate", json={"event": {"entity_id": "alex.smith1@bip.com"}, "hybrid_anomaly_score": 0.20})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("context_assessment", data)

    async def test_get_context_history_api(self):
        response = await self.client.get("/api/v1/context/history")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("metrics", data)

    async def test_get_reasoning_trace_api(self):
        response = await self.client.get("/api/v1/context/reasoning/EMP-1001")
        self.assertEqual(response.status_code, 200)

    async def test_get_trust_breakdown_api(self):
        response = await self.client.get("/api/v1/context/trust/EMP-1001")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
