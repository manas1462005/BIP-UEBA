from typing import Dict, Any, List


class ContextAssessmentEngine:
    """Synthesizes context assessments & structured machine-readable reasoning traces."""

    @staticmethod
    def synthesize_assessment(
        hybrid_score: float,
        trust: Dict[str, Any],
        relationship: Dict[str, Any],
        calendar: Dict[str, Any],
        policy: Dict[str, Any],
        criticality: Dict[str, Any]
    ) -> Dict[str, Any]:
        
        supporting_evidence: List[str] = []
        contradicting_evidence: List[str] = []
        reasoning_trace: List[Dict[str, Any]] = []

        # Step 1: Anomaly Input
        reasoning_trace.append({
            "step": 1,
            "factor": "Hybrid Anomaly Input",
            "evaluation": f"Raw Ensemble Score: {hybrid_score:.3f}",
            "impact": "Anomaly Detected" if hybrid_score > 0.5 else "Low Anomaly Variance"
        })

        # Step 2: Trust Evaluation
        if trust["is_managed_device"] and trust["mfa_verified"]:
            supporting_evidence.append("Hardware compliance & MFA verification confirm identity trust")
            reasoning_trace.append({
                "step": 2,
                "factor": "Trust Reasoning",
                "evaluation": "Managed Hardware + Enforced MFA",
                "impact": "Mitigates Identity Risk"
            })
        else:
            contradicting_evidence.append("Unmanaged hardware or unverified MFA increases identity risk")
            reasoning_trace.append({
                "step": 2,
                "factor": "Trust Reasoning",
                "evaluation": "Unmanaged / Untrusted Hardware Context",
                "impact": "Amplifies Identity Risk"
            })

        # Step 3: Calendar Evaluation
        if calendar["calendar_justified"]:
            supporting_evidence.append(f"Activity aligns with {calendar['schedule_context']}")
            reasoning_trace.append({
                "step": 3,
                "factor": "Calendar Reasoning",
                "evaluation": calendar["schedule_context"],
                "impact": "Mitigates Off-Hours Variance"
            })
        elif calendar["is_off_hours"]:
            contradicting_evidence.append("Off-hours activity occurs outside any scheduled maintenance or release window")
            reasoning_trace.append({
                "step": 3,
                "factor": "Calendar Reasoning",
                "evaluation": "Unscheduled Off-Hours Activity",
                "impact": "Amplifies Temporal Risk"
            })

        # Step 4: Policy & Relationship
        if relationship["is_expected_resource"]:
            supporting_evidence.append("Target resource matches direct project/role assignment")
            reasoning_trace.append({
                "step": 4,
                "factor": "Relationship & Policy",
                "evaluation": "Legitimate RBAC / Project Assignment",
                "impact": "Mitigates Access Risk"
            })

        # Determine final Assessment
        if hybrid_score > 0.5 and len(contradicting_evidence) >= 2:
            assessment = "Unjustified High-Risk Deviation"
            confidence = 0.92
        elif hybrid_score > 0.5 and supporting_evidence:
            assessment = "Contextually Mitigated Operational Activity"
            confidence = 0.88
        else:
            assessment = "Verified Normal Activity Baseline"
            confidence = 0.95

        return {
            "context_assessment": assessment,
            "context_confidence": confidence,
            "hybrid_anomaly_score": hybrid_score,
            "supporting_evidence": supporting_evidence,
            "contradicting_evidence": contradicting_evidence,
            "reasoning_trace": reasoning_trace,
            "trust_summary": trust["trust_level"],
            "calendar_summary": calendar["schedule_context"],
            "business_impact": criticality["business_impact"]
        }
