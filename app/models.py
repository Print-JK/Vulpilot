from typing import Any

from pydantic import BaseModel, Field


class RawFinding(BaseModel):
    title: str

    host: str

    tool: str

    port: int | None = None

    description: str | None = None

    evidence: dict[str, Any] = Field(default_factory=dict)


class Finding(BaseModel):
    title: str

    severity: str

    host: str

    tool: str

    port: int | None = None

    description: str | None = None

    evidence: dict[str, Any] = Field(default_factory=dict)

    recommendation: str | None = None

    detected_by: list[str] = Field(default_factory=list)

    cwe: str | None = None

    mitre: str | None = None