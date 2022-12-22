"""
fmts.transformer
----------------

This module implements functions that transform whois
data into computer-readable data.
"""
import json

try:
    import tomlkit
except ImportError as e:
    print(f"error: {e} (did you installed requirements.txt?)")
    exit(1)

def fmt_json(data):
    return json.dumps(
        json.loads(str(data)),
        indent=2
    )

# TODO: implememnt dict -> toml transformation
def fmt_toml(data):
    ...

implemented_formats = {
    "json": fmt_json,
    "toml": fmt_toml
}

def transform(data, fmt):
    try:
        _transformer = implemented_formats[fmt]
        transformed = _transformer(data)
    except KeyError:
        raise NotImplementedError(f"format {fmt} was not implemented")

    return transformed
