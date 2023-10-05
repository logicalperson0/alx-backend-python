#!/usr/bin/env python3
"""
a type-annotated file
"""


def sum_list(input_list: list[float]) -> float:
    """ type-annotated function sum_list which takes a list input_list
    of floats as argument and returns their sum as a float."""
    return sum(input_list)
