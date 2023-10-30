#!/usr/bin/env python3
"""
a module with class: TestAccessNestedMap to test
utils.access_nested_map function
"""
import unittest
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized
from unittest.mock import patch, Mock
import requests


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        the assertRaises context manager to test that a KeyError is raised
        """
        # actual = access_nested_map(nested_map, path)

        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_url):
        """method to test that utils.get_json returns the expected result"""
        # actual = get_json(test_url)
        mock_url.return_value = Mock()
        # print(Mock())
        mock_url.return_value.json.return_value = test_payload
        actual = get_json(test_url)
        print(actual)
        # print(mock_url)
        mock_url.assert_called_once_with(test_url)
        self.assertEqual(actual, test_payload)


class TestMemoize(unittest.TestCase):
    """class that inherits from unittest.TestCase"""

    def test_memoize(self):
        """method to test utils.memoize decorator"""
        class TestClass:

            def a_method(self):
                return 42

            # @patch.object(TestClass, "a_method")
            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as prop_obj:
            test_class = TestClass()
            res1 = test_class.a_property
            # print(res1)
            res2 = test_class.a_property
            # print(res2)

            self.assertEqual(res1, res2)
            test_class.a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
