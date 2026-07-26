import json
from typing import Dict, Any


class ProfileSerializer:
    """JSON and Pydantic serialization tools for behavioral profiles."""

    @staticmethod
    def serialize_to_json(profile: Dict[str, Any]) -> str:
        return json.dumps(profile, indent=2, default=str)

    @staticmethod
    def deserialize_from_json(json_str: str) -> Dict[str, Any]:
        return json.loads(json_str)
