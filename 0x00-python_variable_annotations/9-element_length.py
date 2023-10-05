#!/usr/bin/env python3
"""
a type-annotated file
"""
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This is the return of the function which is list"""
    return [(i, len(i)) for i in lst]
