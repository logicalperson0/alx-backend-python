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
from mock import PropertyMock


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

    def test_public_repos_url(self):
        """method to unit-test GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient',
                   new_callable=PropertyMock) as prop:
            prop.return_value = {
                'repos_url': 'https://api.github.com/orgs/google'}

            actual = GithubOrgClient('google')._public_repos_url

            self.assertEqual(actual,
                             'https://api.github.com/orgs/google/repos')

    @patch("client.get_json")
    def test_public_repos(self, mock_url):
        """to unit-test GithubOrgClient.public_repos"""
        with patch('client.GithubOrgClient',
                   new_callable=PropertyMock) as props:
            props.return_value = 'https://api.github.com/orgs/google'

            actual = GithubOrgClient("google").public_repos()

            self.assertEqual(actual, "google")

            props.assert_called_once()
            mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, supposed):
        """unit-test GithubOrgClient.has_license"""
        test_goo = GithubOrgClient("google").has_license(repo, license_key)

        self.assertEqual(test_goo, supposed)
