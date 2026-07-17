SEVERITY_ORDER = [
    "Critical",
    "High",
    "Medium",
    "Low",
    "Informational",
]


def build_summary(findings):

    counts = {
        level: 0
        for level in SEVERITY_ORDER
    }

    for finding in findings:
        counts[finding.severity] += 1

    total = len(findings)

    hosts = len(
        {
            f.host
            for f in findings
        }
    )

    if counts["Critical"] == 0 and counts["High"] == 0:
        return (
            f"The assessment covered {hosts} host(s) and identified "
            f"{total} finding(s). No critical or high-severity "
            "findings were detected."
        )

    return (
        f"The assessment covered {hosts} host(s) and identified "
        f"{total} finding(s), including "
        f"{counts['Critical']} Critical and "
        f"{counts['High']} High severity findings."
    )