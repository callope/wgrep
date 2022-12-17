"""
formats.py
----------

Implementation of all the supported parsers.
"""
import json


def fmt_json(data, output_file):
    parsed = json.loads(str(data))
    json.dump(parsed, output_file, indent=2)


def fmt_toml(data, output_file):
    ...


implemented_formats = {
    "json": fmt_json,
    "toml": fmt_toml
}
