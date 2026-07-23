from pydantic import BaseModel
from app.models import Finding


class ReportMetadata(BaseModel):
    generated_on: str
    scope: list[str]


class ExecutiveSummary(BaseModel):
    text: str


class Report(BaseModel):
    metadata: ReportMetadata
    summary: ExecutiveSummary
    findings: list[Finding]