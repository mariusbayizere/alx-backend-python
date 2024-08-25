#!/usr/bin/env python3
"""
Module to test the `utils.access_nested_map` function.
"""

from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the `access_nested_map` function from the `utils` module.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple,
                               expected: any) -> None:
        """
        Test that `access_nested_map` returns the expected output.

        :param nested_map: The nested map (dictionary) to access.
        :param path: The path (tuple) to navigate within the nested map.
        :param expected: The expected value from the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: dict,
                                         path: tuple) -> None:
        """
        Test that `access_nested_map` raises a KeyError for invalid paths.

        :param nested_map: The nested map (dictionary) to access.
        :param path: The path (tuple) to navigate within the nested map.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), str(path[-1]))


if __name__ == "__main__":
    unittest.main()
