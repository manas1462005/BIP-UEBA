import unittest
import httpx
from app.main import app
from app.ai.explainability.grounding_engine import GroundingEngine
from app.ai.explainability.timeline_builder import TimelineBuilder
from app.ai.explainability.executive_summary import ExecutiveSummaryEngine
from app.ai.explainability.technical_summary import TechnicalSummaryEngine
from app.ai.explainability.recommendation_engine import RecommendationEngine
from app.ai.explainability.citation_engine import CitationEngine
from app.ai.explainability.copilot_engine import AnalystCopilotEngine
from app.ai.explainability.explainability_repository import ExplainabilityRepository


class TestExplainabilityEngine(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transport = httpx.ASGITransport(app=app)
        self.client = httpx.AsyncClient(transport=self.transport, base_url="http://test")

    async def asyncTearDown(self):
        await self.client.aclose()

    def test_grounding_engine(self):
        pkg = GroundingEngine.build_evidence_package(
            {"entity_id": "alex.smith1@bip.com", "event_id": "evt_1"},
            {"primary_classification": {"primary_threat_category": "Credential Compromise"}}
        )
        self.assertEqual(pkg["entity_id"], "alex.smith1@bip.com")
        self.assertIn("evidence_graph", pkg)

    def test_timeline_builder(self):
        pkg = {"entity_id": "alex.smith1@bip.com", "primary_category": "Credential Compromise"}
        timeline = TimelineBuilder.build_timeline(pkg)
        self.assertGreater(len(timeline), 0)

    def test_executive_summary(self):
        pkg = {"entity_id": "alex.smith1@bip.com", "primary_category": "Credential Compromise"}
        summary = ExecutiveSummaryEngine.generate_summary(pkg)
        self.assertIn("what_happened", summary)

    def test_technical_summary_and_citations(self):
        pkg = {"entity_id": "alex.smith1@bip.com", "primary_category": "Credential Compromise"}
        narrative = TechnicalSummaryEngine.generate_narrative(pkg)
        cited = CitationEngine.attach_citations(narrative["technical_narrative"], pkg)
        self.assertIn("citations", cited)

    def test_recommendation_engine(self):
        pkg = {"entity_id": "alex.smith1@bip.com", "primary_category": "Credential Compromise"}
        recs = RecommendationEngine.generate_recommendations(pkg)
        self.assertGreater(len(recs), 0)

    def test_copilot_engine(self):
        pkg = {"event_id": "evt_1", "entity_id": "alex.smith1@bip.com", "primary_category": "Credential Compromise"}
        res = AnalystCopilotEngine.answer_query("Why was this event classified as Credential Compromise?", pkg)
        self.assertTrue(res["evidence_grounded"])
        self.assertIn("answer", res)

    async def test_generate_explanation_api(self):
        response = await self.client.post("/api/v1/explain/generate", json={"event": {"entity_id": "alex.smith1@bip.com"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("executive_summary", data)

    async def test_copilot_api(self):
        response = await self.client.post("/api/v1/explain/copilot", json={"event": {"entity_id": "alex.smith1@bip.com"}, "query": "Why was this classified?"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("answer", data)

    async def test_get_timeline_api(self):
        response = await self.client.get("/api/v1/explain/timeline/EMP-1001")
        self.assertEqual(response.status_code, 200)

    async def test_get_evidence_graph_api(self):
        response = await self.client.get("/api/v1/explain/evidence/EMP-1001")
        self.assertEqual(response.status_code, 200)

    async def test_get_recommendations_api(self):
        response = await self.client.get("/api/v1/explain/recommendations/EMP-1001")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
