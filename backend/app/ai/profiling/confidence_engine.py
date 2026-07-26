from typing import List, Dict, Any


class ConfidenceEngine:
    """Computes profile confidence score [0.0, 1.0] based on history length, volume, & stability."""

    @staticmethod
    def calculate_confidence(extracted_features: List[Dict[str, Any]]) -> Dict[str, Any]:
        count = len(extracted_features)
        
        # History & volume score
        volume_score = min(1.0, count / 50.0)
        
        # Data completeness
        completeness_score = 1.0 if count > 0 and "source_ip" in extracted_features[0] else 0.5
        
        # Stability score
        stability_score = 0.90 if count >= 10 else 0.60
        
        overall_confidence = round(0.5 * volume_score + 0.3 * completeness_score + 0.2 * stability_score, 2)

        return {
            "confidence_score": overall_confidence,
            "confidence_tier": "High" if overall_confidence >= 0.8 else ("Medium" if overall_confidence >= 0.5 else "Low"),
            "sample_count": count,
            "data_completeness": completeness_score,
            "behavior_stability": stability_score
        }
