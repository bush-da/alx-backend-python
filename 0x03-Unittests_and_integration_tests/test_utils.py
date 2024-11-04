#!/usr/bin/python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap is a test class for testing the `access_nested_map` function.

    The function `access_nested_map` takes a nested dictionary (or map) and a sequence of keys (path).
    It returns the value found at the end of the path within the nested dictionary.

    This class tests `access_nested_map` with different inputs to verify that it returns
    the expected values for valid paths.

    Methods
    -------
    test_access_nested_map(nested_map, path, expected):
        Tests the `access_nested_map` function with different `nested_map` and `path`
        parameters, verifying that it returns `expected` values.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test `access_nested_map` with different inputs.

        Parameters
        ----------
        nested_map : dict
            A nested dictionary to be tested.
        path : tuple
            A tuple representing the sequence of keys to access within `nested_map`.
        expected : Any
            The expected result from `access_nested_map` for the given `nested_map` and `path`.

        This test method checks that the `access_nested_map` function returns the expected
        value for each set of inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
