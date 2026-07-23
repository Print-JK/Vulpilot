from pathlib import Path

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

    return template.render(
        report=report,
        severity_counts=severity_counts,
    )