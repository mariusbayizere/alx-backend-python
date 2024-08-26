#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient  # Ensure this module is present
import fixtures  # Assuming fixtures.py contains the necessary data


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


@parameterized_class([
    {
        "org_payload": fixtures.ORG_PAYLOAD,
        "repos_payload": fixtures.REPOS_PAYLOAD,
        "expected_repos": fixtures.EXPECTED_REPOS,
        "apache2_repos": fixtures.APACHE2_REPOS,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Setup the mock for requests.get."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Return different fixtures based on the URL."""
            if url == f"https://api.github.com/orgs/google":
                return cls.org_payload
            elif url == f"https://api.github.com/orgs/google/repos":
                return cls.repos_payload
            return None

        cls.mock_get.return_value.json.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method."""
        client = GithubOrgClient('google')
        repos = client.public_repos()

        # Ensure the repos match the expected list
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with license filtering."""
        client = GithubOrgClient('google')
        repos = client.public_repos(license="apache-2.0")

        # Ensure the repos match the expected list of repos with the Apache-2.0
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
