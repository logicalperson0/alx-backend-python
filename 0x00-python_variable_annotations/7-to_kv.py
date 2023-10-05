#!/usr/bin/env python3
"""
a type-annotated file
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """type-annotated function to_kv that takes a string k and an int OR
    float v as arguments and returns a tuple."""
    if (v == int):
        v = float(v)
    c = v ** 2
    tup = (k, c)

    return tup
