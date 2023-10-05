#!/usr/bin/env python3
"""
a type-annotated file
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by
    multiplier"""

    def multi_float(multi: float) -> float:
        """Multiples the parameter with the parent function parameter"""
        return multi * multiplier

    return multi_float
