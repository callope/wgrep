"""
files.py
--------

File utilities for this tool.
"""
import os
from os import path
from shutil import rmtree


# def rootname(dest: str):
#     """
#     Will return the root of a path.
#     """

#     while True:
#         if path.dirname(dest) in ['/', '']:
#             break
#         if dest.split('/') == 2:
#             break
#         dest = path.dirname(dest)

#     return dest


def remove_path(dest: str):
    """
    Will remove the destination completely, erasing
    all the folders and files from it (if dest is
    ./a/b/c/d.xml, remove_path will act like `rm -rf
    ./a`)
    """


def ensure_path(dest: str):
    """
    Will ensure the folder hierarchy to a path
    (if parent folders do not exist, it will
    create them.)
    """
    os.makedirs(path.dirname(dest), exist_ok=True)
