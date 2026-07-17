TITLE_ALIASES = {
    "ssh service": "ssh",
    "openssh": "ssh",
    "http service": "http",
    "apache http server": "http",
    "https service": "https",
}


def normalize_title(title: str) -> str:
    return TITLE_ALIASES.get(title.strip().lower(), title.strip().lower())