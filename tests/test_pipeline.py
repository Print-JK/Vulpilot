from app.parsers.factory import ParserFactory
from app.services.pipeline import process_all
from app.services.deduplicate import DuplicateDetectionService


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

    print(f"\nMerged Findings: {len(merged)}\n")

    for finding in merged:
        print(finding.model_dump())
        print("-" * 70)


if __name__ == "__main__":
    main()