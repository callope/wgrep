import argparse
from argparse import ArgumentParser

_parser = ArgumentParser(
    "wgrep",
    description="""Save whois information into a computer-readable file format (like toml, json, xml, etc.)"""
)

_parser.add_argument(
    'target',
    metavar='target',
    help="""The target to execute lookup."""
)

_parser.add_argument(
    'output',
    metavar="output",
    default='wgrep.out',
    help="""The file to save the output."""
)

_parser.add_argument(
    'format',
    metavar="format",
    help="""The format to save the data."""
)

args = _parser.parse_args()
