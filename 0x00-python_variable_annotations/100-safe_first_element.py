#!/usr/bin/env python3
"""
a duck typed file
"""
from typing import List, Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the 1st value of the parameter"""
    if lst:
        return lst[0]
    else:
        return None
