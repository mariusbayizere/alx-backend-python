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

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """
        Test the public_repos method.
        Ensures that get_json is called with the correct URL,
        and the repos are returned as expected.
        """
        mock_repos_url.return_value = (
            'https://api.github.com/orgs/google/repos'
        )
        mock_get_json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]

        client = GithubOrgClient('google')
        result = client.public_repos()

        # Test that the result matches the expected list of repo names
        self.assertEqual(result, ['repo1', 'repo2'])

        # Test that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/google/repos'
        )

        # Test that the mocked property _public_repos_url was accessed once
        mock_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test the has_license method.
        Ensure it returns the correct boolean value depending on the license.
        """
        client = GithubOrgClient('google')
        self.assertEqual(client.has_license(repo, license_key), expected)


if __name__ == "__main__":
    unittest.main()
