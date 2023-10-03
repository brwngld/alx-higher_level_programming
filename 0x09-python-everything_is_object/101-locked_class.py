#!/usr/bin/python3
"""A class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance
attributes, exceptif the new instance attribute is called first_name."""


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
