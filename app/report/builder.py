from datetime import datetime

from app.report.models import (
    ExecutiveSummary,
    Report,
    ReportMetadata,
)


def build_report(findings):

    metadata = ReportMetadata(
        generated_on=datetime.now().strftime("%Y-%m-%d %H:%M"),
        scope=sorted({f.host for f in findings}),
    )

    summary = ExecutiveSummary(
        text=build_summary(findings)
    )

    return Report(
        metadata=metadata,
        summary=summary,
        findings=findings,
    )