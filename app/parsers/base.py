from abc import ABC, abstractmethod
from pathlib import Path

from app.models import RawFinding


class BaseParser(ABC):
    """Base interface for all scanner parsers."""

    @abstractmethod
    def parse(self, file_path: str | Path) -> list[RawFinding]:
        """Parse a scanner output into RawFinding objects."""
        raise NotImplementedError