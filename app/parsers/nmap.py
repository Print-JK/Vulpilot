from pathlib import Path
import xml.etree.ElementTree as ET

from app.models import RawFinding
from app.parsers.base import BaseParser


class NmapParser(BaseParser):

    def parse(self, file_path: str | Path) -> list[RawFinding]:

        findings: list[RawFinding] = []

        tree = ET.parse(file_path)
        root = tree.getroot()

        for host in root.findall("host"):

            address = host.find("address")

            if address is None:
                continue

            host_ip = address.attrib.get("addr", "Unknown")

            ports = host.find("ports")

            if ports is None:
                continue

            for port in ports.findall("port"):

                state = port.find("state")

                if state is None:
                    continue

                if state.attrib.get("state") != "open":
                    continue

                service = port.find("service")

                service_name = None
                product = None
                version = None

                if service is not None:
                    service_name = service.attrib.get("name")
                    product = service.attrib.get("product")
                    version = service.attrib.get("version")

                findings.append(
                    RawFinding(
                        title=service_name or "unknown",
                        host=host_ip,
                        tool="nmap",
                        port=int(port.attrib["portid"]),
                        description="Service detected by Nmap.",
                        evidence={
                            "service": service_name,
                            "product": product,
                            "version": version,
                            "state": "open",
                        },
                    )
                )

        return findings