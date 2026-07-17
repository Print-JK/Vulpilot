from pydantic import BaseModel

from app.models import Finding


class ReportMetadata(BaseModel):
    title: str = "Vulpilot Security Assessment Report"

    generated_by: str = "Vulpilot"

    generated_on: str

    scope: list[str]


class ExecutiveSummary(BaseModel):
    text: str


class Report(BaseModel):
    metadata: ReportMetadata

    summary: ExecutiveSummary

    findings: list[Finding]