from datetime import datetime

from app.ai.service import AIService
from app.report.models import (
    ExecutiveSummary,
    Report,
    ReportMetadata,
)
from app.report.summary import build_summary


def build_report(findings):
    metadata = ReportMetadata(
        generated_on=datetime.now().strftime("%Y-%m-%d %H:%M"),
        scope=sorted({f.host for f in findings}),
    )

    try:
        summary_text = AIService.generate(findings)
    except Exception as e:
        print(f"[AI] Falling back to deterministic summary: {e}")
        summary_text = build_summary(findings)

    return Report(
        metadata=metadata,
        summary=ExecutiveSummary(text=summary_text),
        findings=findings,
    )