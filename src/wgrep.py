"""
wgrep
-----

A simple tool to save whois information onto a computer-readable
file (json, toml, etc)
"""
from parser import args
from utils import save_to_file
from fmts import transform
from whois import whois


_lnk = args.target
_out = args.output
_fmt = args.format

try:
    data = whois(_lnk)
    formatted = transform(data, _fmt)
    save_to_file(formatted, _out)

except Exception as e: # handle unexpected exceptions
    print(f"error: {e}")
except KeyboardInterrupt as e:
    ...
