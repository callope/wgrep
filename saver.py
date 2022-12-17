"""
saver.py
--------

This is pretty much the core of the tool, it will execute
the lookup and save the output in a file with desired fmt.
"""
from files import ensure_path, remove_path
from fmts import save_to_file
from whois import whois


def save(lnk: str, out: str, fmt: str):
    """
    Will save the whois output into a file
    with the desired format.

    Args:
        lnk: str    - the lookup target
        out: str    - the output file
        fmt: str    - the output format
    """

    try:
        ensure_path(out)

        with open(out, '+w') as file:
            data = whois(lnk)
            save_to_file(data, file, fmt)
    except NotImplementedError as e:
        remove_path(out)
        print(f"error: {e}")
