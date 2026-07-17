from __future__ import annotations

import json
from pathlib import Path

from app.models import RawFinding
from app.parsers.base import BaseParser


class NucleiParser(BaseParser):
    """Parser for Nuclei JSONL output."""

    def parse(self, file_path: str | Path) -> list[RawFinding]:
        findings: list[RawFinding] = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                result = json.loads(line)

                info = result.get("info", {})

                findings.append(
                    RawFinding(
                        title=info.get("name", "Unknown Finding"),
                        host=result.get("host", "Unknown"),
                        tool="nuclei",
                        description="Finding reported by Nuclei.",
                        evidence={
                            "template_id": result.get("template-id"),
                            "severity": info.get("severity"),
                            "matched_at": result.get("matched-at"),
                            "classification": info.get("classification", {}),
                            "tags": result.get("tags", []),
                        },
                    )
                )

        return findings