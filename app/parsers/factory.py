from app.parsers.nmap import NmapParser
from app.parsers.nuclei import NucleiParser


class ParserFactory:

    _parsers = {
        "nmap": NmapParser,
        "nuclei": NucleiParser,
    }

    @classmethod
    def create(cls, scanner: str):

        try:
            return cls._parsers[scanner.lower()]()

        except KeyError as exc:
            raise ValueError(f"Unsupported scanner: {scanner}") from exc