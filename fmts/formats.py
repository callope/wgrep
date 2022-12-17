"""
formats.py
----------

Implementation of all the supported parsers.
"""
import json


def fmt_json(data, output_file):
    """Will parse whois data to JSON format."""
    parsed = json.loads(str(data))
    json.dump(parsed, output_file, indent=2)


def fmt_toml(data, output_file):
    """Will parse whois data to TOML format."""
    ...


implemented_formats = {
    "json": fmt_json,
    "toml": fmt_toml
}
