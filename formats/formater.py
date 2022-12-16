"""
formater.py
-----------

The little module responsible for formatting the output
of whois information.
"""


format_table = {
    "json": None,
    "toml": None,
}

def format_output(data, fmt):
    try:
        print(format_table[fmt])
    except KeyError:
        raise NotImplementedError(f"{fmt} format was not implemented.")
