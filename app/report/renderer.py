from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader


TEMPLATE_DIR = Path(__file__).parent / "templates"

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=True,
)


def generate_html(report):
    template = env.get_template("report.html")

    severity_counts = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0,
        "Informational": 0,
        "Unknown": 0,
    }

    for finding in report.findings:
        severity_counts[finding.severity] += 1

    # Convert AI summary Markdown to HTML
    summary_html = markdown.markdown(
        report.summary.text,
        extensions=[
            "tables",
            "fenced_code",
            "nl2br",
        ],
    )

    return template.render(
        report=report,
        severity_counts=severity_counts,
        summary_html=summary_html,
    )