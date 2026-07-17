from pathlib import Path
from weasyprint import HTML


def export_pdf(html: str, output_path: str | Path):
    """
    Convert rendered HTML into a PDF.
    """

    HTML(string=html).write_pdf(str(output_path))