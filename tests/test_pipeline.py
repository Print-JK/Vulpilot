from app.parsers.factory import ParserFactory
from app.services.pipeline import process_all
from app.services.deduplicate import DuplicateDetectionService
from app.report.renderer import generate_html


def run_test(scanner: str, file_path: str):
    parser = ParserFactory.create(scanner)

    raw_findings = parser.parse(file_path)

    return process_all(raw_findings)


def main():
    findings = []

    findings.extend(
        run_test(
            "nmap",
            "sample_scans/nmap.xml",
        )
    )

    merged = DuplicateDetectionService.merge(findings)
    
    html = generate_html(merged)

    with open("report.html", "w", encoding="utf-8") as report:
        report.write(html)

    print("Generated report.html")  

if __name__ == "__main__":
    main()