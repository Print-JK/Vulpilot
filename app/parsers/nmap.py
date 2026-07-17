from pathlib import Path
from typing import List
import xml.etree.ElementTree as ET

from app.models import Finding


def parse_nmap(file_path: str | Path) -> List[Finding]:
    findings: List[Finding] = []
    
    try:
        tree = ET.parse(file_path)
    except ET.ParseError as e:
        raise ValueError(f"Invalid Nmap XML file:{e}") from e
    
    
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

            state_value = state.attrib.get("state")

            if state_value != "open":
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
                Finding(
                    title=service_name or "unknown",
                    severity="Informational",
                    host=host_ip,
                    port=int(port.attrib["portid"]),
                    description="Service detected by Nmap.",
                    evidence={
                        "service": service_name,
                        "product": product,
                        "version": version,
                        "state": state_value,
                    },
                    tool="nmap",
                    detected_by=["nmap"],
                )
            )

    return findings