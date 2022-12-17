"""
files.py
--------

File utilities for this tool.
"""
import os
from os import path

from pathlib import Path
from shutil import rmtree


def rootname(dest: str):
    """
    Will return the root of a path.
    """
    p = Path(dest)

    return path.join(
        p.parents[len(p.parents) - 1],
        p.parents[len(p.parents) - 2]
    )


def remove_path(dest: str):
    """
    Will remove the destination completely, erasing
    all the folders and files from it (if dest is
    ./a/b/c/d.xml, remove_path will act like `rm -rf
    ./a`)
    """
    rmtree(rootname(dest), ignore_errors=True)


def ensure_path(dest: str):
    """
    Will ensure the folder hierarchy to a path
    (if parent folders do not exist, it will
    create them.)
    """
    os.makedirs(path.dirname(dest), exist_ok=True)
