#!/usr/bin/env python3
"""
This module contains the unit tests for client.py
"""
from typing import List, Dict
from parameterized import parameterized
from unittest.mock import patch, Mock
import unittest

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class for testing GithubOrgClient
    """
    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json')
    def test_org(
                 self,
                 org: str,
                 expected: Dict,
                 mocked_get_json: Mock
                 ) -> None:
        """
        Test that GithubOrgClient.org returns the correct value
        """
        mocked_get_json.return_value = expected
        org_client: GithubOrgClient = GithubOrgClient(org)
        self.assertEqual(org_client.org, expected)
        mocked_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
