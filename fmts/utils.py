"""
utils.py
--------

Utilitie functions.
"""
from .formats import implemented_formats


def save_to_file(data, output_file, fmt):
    try:
        implemented_formats[fmt](data, output_file)
    except KeyError:
        raise NotImplementedError(f"the solicited format ({fmt}) was not implemented.")
