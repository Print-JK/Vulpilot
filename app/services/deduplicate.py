from app.models import Finding
from app.utils.title import normalize_title


SEVERITY_ORDER = {
    "Critical": 5,
    "High": 4,
    "Medium": 3,
    "Low": 2,
    "Informational": 1,
    "Unknown": 0,
}


class DuplicateDetectionService:
    @staticmethod
    def merge(findings: list[Finding]) -> list[Finding]:
        merged: dict[tuple[str, int | None, str], Finding] = {}

        for finding in findings:
            key = (
                finding.host,
                finding.port,
                normalize_title(finding.title),
            )

            if key not in merged:
                merged[key] = finding
                continue

            existing = merged[key]

            # Merge scanner list
            existing.detected_by = sorted(
                set(existing.detected_by + finding.detected_by)
            )

            # Keep the higher severity
            if (
                SEVERITY_ORDER[finding.severity]
                > SEVERITY_ORDER[existing.severity]
            ):
                existing.severity = finding.severity

        return list(merged.values())