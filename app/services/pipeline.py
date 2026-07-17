from app.models import Finding, RawFinding
from app.services.severity import SeverityNormalizer


def process(raw: RawFinding) -> Finding:
    return Finding(
        title=raw.title,
        severity=SeverityNormalizer.normalize(raw),
        host=raw.host,
        tool=raw.tool,
        port=raw.port,
        description=raw.description,
        evidence=raw.evidence,
        detected_by=[raw.tool],
    )


def process_all(raw_findings: list[RawFinding]) -> list[Finding]:
    return [process(raw) for raw in raw_findings]