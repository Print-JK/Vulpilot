from dataclasses import dataclass

from app.models import Finding


@dataclass
class ReportContext:
    title: str
    generated_by: str
    generated_on: str

    scope: list[str]

    findings: list[Finding]