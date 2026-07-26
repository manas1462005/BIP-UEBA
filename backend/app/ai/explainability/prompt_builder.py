from typing import Dict, Any


class PromptBuilder:
    """Constructs system prompts enforcing 100% evidence grounding rules for LLM / generator."""

    @staticmethod
    def build_system_prompt() -> str:
        return (
            "You are an enterprise AI Cybersecurity Analyst Assistant for the Behavioral Intelligence Platform.\n"
            "CRITICAL RULES:\n"
            "1. You MUST operate ONLY on the provided structured Evidence Package.\n"
            "2. NEVER invent evidence, change threat classifications, or alter confidence metrics.\n"
            "3. Every statement must reference specific evidence signals, detector scores, or MITRE technique IDs.\n"
            "4. If evidence is unavailable for a user question, explicitly state 'Unavailable in structured evidence package'."
        )

    @staticmethod
    def build_explanation_prompt(evidence_package: Dict[str, Any]) -> str:
        return f"Generate an evidence-grounded SOC analyst explanation for event '{evidence_package.get('event_id')}' using the following evidence package:\n{evidence_package}"
