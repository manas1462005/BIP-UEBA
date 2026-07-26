from typing import Dict, Any
from app.ai.context.trust_reasoning import TrustReasoningEngine
from app.ai.context.relationship_reasoning import RelationshipReasoningEngine
from app.ai.context.calendar_reasoning import CalendarReasoningEngine
from app.ai.context.policy_reasoning import PolicyReasoningEngine
from app.ai.context.business_criticality import BusinessCriticalityEngine
from app.ai.context.context_assessment import ContextAssessmentEngine


class ReasoningPipeline:
    """Modular context reasoning execution pipeline."""

    @staticmethod
    def execute(event: Dict[str, Any], profile: Dict[str, Any], hybrid_score: float) -> Dict[str, Any]:
        trust = TrustReasoningEngine.evaluate_trust(event, profile)
        rel = RelationshipReasoningEngine.evaluate_relationships(event, profile)
        cal = CalendarReasoningEngine.evaluate_calendar(event, profile)
        policy = PolicyReasoningEngine.evaluate_policy(event, profile)
        crit = BusinessCriticalityEngine.evaluate_criticality(event, profile)

        assessment = ContextAssessmentEngine.synthesize_assessment(
            hybrid_score=hybrid_score,
            trust=trust,
            relationship=rel,
            calendar=cal,
            policy=policy,
            criticality=crit
        )

        assessment["details"] = {
            "trust": trust,
            "relationship": rel,
            "calendar": cal,
            "policy": policy,
            "criticality": crit
        }

        return assessment
