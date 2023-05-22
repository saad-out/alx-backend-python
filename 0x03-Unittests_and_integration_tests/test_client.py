#!/usr/bin/env python3
"""
This module contains the unit tests for client.py
"""
from typing import List, Dict
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
import unittest

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mocked_org: Mock):
        """
        Test that the result of _public_repos_url is the expected one
        """
        payload = {
            "login": "google",
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        mocked_org.return_value = payload
        org_client: GithubOrgClient = GithubOrgClient("google")
        self.assertEqual(org_client._public_repos_url, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(
                          self,
                          mocked_get_json: Mock
                          ) -> None:
        """
        Test that the list of repos is what you expect from the chosen payload
        """
        REPOS_URL = "https://api.github.com/orgs/google/repos"
        repos = [
            {"id": 1, "name": "truth"},
            {"id": 2, "name": "autoparse"},
            {"id": 3, "name": "anvil-build"}
        ]
        mocked_get_json.return_value = repos
        with patch.object(
                          GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock
                          ) as mocked_repos_url:
            mocked_repos_url.return_value = REPOS_URL
            org_client: GithubOrgClient = GithubOrgClient("google")
            self.assertEqual(
                             org_client.public_repos(),
                             [repo["name"] for repo in repos]
                             )
            mocked_repos_url.assert_called_once()
        mocked_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
                         self,
                         repo: Dict[str, Dict],
                         license_key: str,
                         has_license: bool
                        ) -> None:
        """
        Test that GithubOrgClient.has_license returns the correct value
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         has_license)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [
        (TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1],
         TEST_PAYLOAD[0][2], TEST_PAYLOAD[0][3])
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Class for testing GithubOrgClient integrated with fixtures.py
    """
    def setUp(self) -> None:
        """Set Up method"""
        self.get_patcher = patch('utils.requests.get')
        self.mocked_get_request = self.get_patcher.start()
        self.mocked_get_request.return_value.json.side_effect = [
            self.org_payload, self.repos_payload
        ]
        self.org_client: GithubOrgClient = GithubOrgClient("google")

    def tearDown(self) -> None:
        """Tear Down method"""
        self.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        Test that GithubOrgClient.public_repos returns the correct list of
        repos
        """
        self.assertEqual(self.org_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """
        Test that GithubOrgClient.public_repos returns the correct list of
        repos filtered by license
        """
        self.assertEqual(
                         self.org_client.public_repos("apache-2.0"),
                         self.apache2_repos
                        )


if __name__ == "__main__":
    unittest.main()
