from app.models import RawFinding

SEVERITY_MAP = {
    "critical": "Critical",
    "high": "High",
    "medium": "Medium",
    "low": "Low",
    "info": "Informational",
    "informational": "Informational",
}


class SeverityNormalizer:

    @staticmethod
    def normalize(raw: RawFinding) -> str:

        if raw.tool == "nmap":
            return "Informational"

        if raw.tool == "nuclei":
            severity = raw.evidence.get("severity", "")
            return SEVERITY_MAP.get(
                str(severity).lower(),
                "Informational",
            )

        return "Unknown"