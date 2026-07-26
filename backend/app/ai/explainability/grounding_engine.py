from typing import Dict, Any, List


class GroundingEngine:
    """Collects multi-phase outputs and builds a queryable evidence graph metadata payload."""

    @staticmethod
    def build_evidence_package(
        event: Dict[str, Any],
        threat_assessment: Dict[str, Any]
    ) -> Dict[str, Any]:
        
        entity_id = event.get("entity_id", "alex.smith1@bip.com")
        event_id = event.get("event_id", "evt_sim_99182")
        resource = str(event.get("resource_accessed", "Azure Active Directory"))
        device_id = str(event.get("device_id", "dev_1001"))

        primary_class = threat_assessment.get("primary_classification", {})
        category = primary_class.get("primary_threat_category", "Credential Compromise")
        confidence = primary_class.get("classification_confidence", 0.90)

        mitre_mappings = threat_assessment.get("mitre_mappings", [])
        attack_chain = threat_assessment.get("attack_chain", [])
        hypotheses = threat_assessment.get("ranked_hypotheses", [])
        evidence_summary = threat_assessment.get("evidence_summary", {})

        # Build Evidence Graph Nodes & Edges
        nodes = [
          {"id": f"user:{entity_id}", "type": "User", "label": entity_id},
          {"id": f"device:{device_id}", "type": "Device", "label": device_id},
          {"id": f"resource:{resource}", "type": "Application", "label": resource},
          {"id": f"threat:{category}", "type": "Threat", "label": category}
        ]

        edges = [
          {"source": f"user:{entity_id}", "target": f"device:{device_id}", "relationship": "Authenticated"},
          {"source": f"user:{entity_id}", "target": f"resource:{resource}", "relationship": "Accessed"},
          {"source": f"resource:{resource}", "target": f"threat:{category}", "relationship": "Correlated"}
        ]

        for m in mitre_mappings:
          nodes.append({"id": f"mitre:{m.get('technique_id')}", "type": "MITRE Technique", "label": m.get("technique_name")})
          edges.append({"source": f"threat:{category}", "target": f"mitre:{m.get('technique_id')}", "relationship": "MappedTo"})

        for stage in attack_chain:
          nodes.append({"id": f"stage:{stage.get('stage')}", "type": "Attack Stage", "label": stage.get("tactic")})
          edges.append({"source": f"threat:{category}", "target": f"stage:{stage.get('stage')}", "relationship": "Escalated"})

        return {
            "entity_id": entity_id,
            "event_id": event_id,
            "resource_accessed": resource,
            "primary_category": category,
            "classification_confidence": confidence,
            "evidence_signals": evidence_summary.get("evidence_signals", []),
            "detector_scores": evidence_summary.get("detector_scores", {}),
            "mitre_mappings": mitre_mappings,
            "attack_chain": attack_chain,
            "ranked_hypotheses": hypotheses,
            "reasoning_trace": evidence_summary.get("reasoning_trace", []),
            "evidence_graph": {
                "nodes": nodes,
                "edges": edges,
                "node_count": len(nodes),
                "edge_count": len(edges)
            }
        }
