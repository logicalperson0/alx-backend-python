#!/usr/bin/env python3
"""
a module with class: TestGithubOrgClient to test
client.GithubOrgClient func
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
import requests
from typing import Dict
from unittest.mock import patch, Mock, MagicMock


class TestGithubOrgClient(unittest.TestCase):
    """class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ("google", {"name": "Google"}),
        ("abc", {'name': 'abc'}),
    ])
    @patch('client.get_json')
    def test_org(self, orgs, supposed, mock_fn):
        """ method should test that GithubOrgClient.org returns
        the correct value"""
        mock_fn.return_value = Mock(return_value=supposed)
        # mock_fn.return_value = supposed
        # print(mock_fn)
        actual = GithubOrgClient(orgs).org()
        # print(actual)

        self.assertEqual(actual, supposed)
