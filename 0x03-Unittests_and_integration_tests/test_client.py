#!/usr/bin/env python3
"""
This module contains the unit tests for client.py
"""
from typing import List
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
    def test_org(self, org: str, mocked_get_json: MagicMock) -> None:
        """
        Test that GithubOrgClient.org returns the correct value
        """
        ORG_URL: str = "https://api.github.com/orgs/{}".format(org)
        mocked_get_json.return_value = {"repos_url": ORG_URL + "/repos"}
        org_client: GithubOrgClient = GithubOrgClient(org)
        self.assertEqual(org_client.org, {"repos_url": ORG_URL + "/repos"})
        mocked_get_json.called_once_with(ORG_URL)
