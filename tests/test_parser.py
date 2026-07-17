from app.parsers.nmap import parse_nmap
from app.services.normalize import normalize


def main():
    raw_findings = parse_nmap("sample_scans/nmap.xml")
    findings = [normalize(f) for f in raw_findings]

    print(f"Parsed {len(findings)} findings\n")

    for finding in findings:
        print(finding.model_dump())
        print("-" * 60)


if __name__ == "__main__":
    main()