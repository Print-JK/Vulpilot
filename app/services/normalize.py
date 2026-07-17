from app.models import Finding, RawFinding


DEFAULT_SEVERITY = {
    "nmap": "Informational",
    "nuclei": "Unknown",
}


def normalize(raw: RawFinding) -> Finding:
    return Finding(
        title=raw.title,

        severity=DEFAULT_SEVERITY.get(raw.tool, "Unknown"),

        host=raw.host,

        tool=raw.tool,

        port=raw.port,

        description=raw.description,

        evidence=raw.evidence,

        detected_by=[raw.tool],
    )