from typing import List, Dict, Any


class VersionManager:
    """Manages profile version history, snapshots, and rollbacks with zero overwrite policy."""

    @staticmethod
    def create_version_snapshot(current_profile: Dict[str, Any], previous_version: int = 1) -> Dict[str, Any]:
        new_version = previous_version + 1
        snapshot = dict(current_profile)
        snapshot["version"] = new_version
        snapshot["snapshot_type"] = "Incremental Update Snapshot"
        return snapshot
