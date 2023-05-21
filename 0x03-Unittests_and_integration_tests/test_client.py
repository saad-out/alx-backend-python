#!/usr/bin/env python3
"""
This module contains the unit tests for client.py
"""
from parameterized import parameterized
from unittest.mock import patch, MagicMock
import unittest

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class for testing GithubOrgClient
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mocked_get_json: MagicMock):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        REPOS_URL: str = "https://api.github.com/orgs/{}/repos".format(org)
        mocked_get_json.side_effect = [
            {"repos_url": REPOS_URL},
            [{"name": "{}-repo{}".format(org, i)} for i in range(3)]
        ]
        org_client = GithubOrgClient(org)
        repos = org_client.public_repos()
        self.assertEqual(repos, ["{}-repo{}".format(org, i) for i in range(3)])
        mocked_get_json.called_once_with(REPOS_URL)
