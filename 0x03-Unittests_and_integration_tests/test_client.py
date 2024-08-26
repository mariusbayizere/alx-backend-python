#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient  # Ensure this module is present


class TestGithubOrgClient(unittest.TestCase):
    """Unit test for GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json', return_value={"login": "mock"})
    def test_org(self, org_name, expected_response, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        Ensures get_json is called with the correct argument.
        """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected_response)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that _public_repos_url returns the expected value
        when org is mocked.
        """
        # Mocked payload for the org property
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/google/repos'
        }

        client = GithubOrgClient('google')

        # Test that _public_repos_url returns the expected repos_url
        self.assertEqual(
            client._public_repos_url,
            'https://api.github.com/orgs/google/repos'
        )


if __name__ == "__main__":
    unittest.main()
