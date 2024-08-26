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
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos method.

        Mock get_json to return a predefined payload.
        Mock _public_repos_url to return a custom value.
        Test that public_repos returns the expected list of repos
        and that the mocks were called correctly.
        """
        # Define the mock payload returned by get_json
        mock_payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        mock_get_json.return_value = mock_payload

        # Mock _public_repos_url to return a custom URL
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value='https://api.github.com/orgs/google/repos'):
            client = GithubOrgClient('google')
            repos = client.public_repos()

            # Test the result is as expected
            self.assertEqual(repos, ['repo1', 'repo2', 'repo3'])

            # Ensure the mocked _public_repos_url property was called
            self.assertEqual(client._public_repos_url,
                             'https://api.github.com/orgs/google/repos')

            # Ensure get_json was called once with the correct URL
            mock_get_json.assert_called_once_with(
                'https://api.github.com/orgs/google/repos'
            )


if __name__ == "__main__":
    unittest.main()
