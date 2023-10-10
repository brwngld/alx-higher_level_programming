#!/usr/bin/python3
"""A function that reads a text file (UFT8) and
   prints it out."""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
