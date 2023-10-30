#!/usr/bin/env python3
"""
a module with class: TestAccessNestedMap to test
utils.access_nested_map function
"""
import unittest
from utils import access_nested_map
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """class that inherits from unittest.TestCase"""

    """The 3rd arg is the expected result from the nested_map
        and path args"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, supposed: int) -> None:
        """method to test that the method returns what it is supposed to"""
        actual = access_nested_map(nested_map, path)

        self.assertEqual(actual, supposed)


if __name__ == '__main__':
    unittest.main()
