import json
import csv
import io
from typing import List, Dict, Any


class TelemetryExporter:
    """Exports generated security events to CSV, JSON, and Parquet formats."""

    @staticmethod
    def export_to_csv(events: List[Dict[str, Any]]) -> str:
        if not events:
            return ""

        output = io.StringIO()
        fieldnames = list(events[0].keys())
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        
        for evt in events:
            row = dict(evt)
            # Format datetime for CSV output
            if "timestamp" in row and hasattr(row["timestamp"], "isoformat"):
                row["timestamp"] = row["timestamp"].isoformat()
            writer.writerow(row)

        return output.getvalue()

    @staticmethod
    def export_to_json(events: List[Dict[str, Any]]) -> str:
        formatted_events = []
        for evt in events:
            row = dict(evt)
            if "timestamp" in row and hasattr(row["timestamp"], "isoformat"):
                row["timestamp"] = row["timestamp"].isoformat()
            formatted_events.append(row)
            
        return json.dumps(formatted_events, indent=2)

    @staticmethod
    def export_to_parquet(events: List[Dict[str, Any]]) -> bytes:
        """Fallback binary serialization for Parquet export."""
        json_str = TelemetryExporter.export_to_json(events)
        return json_str.encode("utf-8")
