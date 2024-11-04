#!/usr/bin/env python3
"""A module for testing the utils module.

This module contains unit tests for functions in the `utils` module:
- `access_nested_map`: Tests for accessing nested dictionaries.
- `get_json`: Tests for retrieving JSON data from URLs.
- `memoize`: Tests for caching results of method calls.
"""

import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function.

    This class tests the behavior of `access_nested_map` for:
    - Successfully retrieving values using valid paths.
    - Raising `KeyError` when accessing invalid paths.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output for valid paths.

        Parameters:
            nested_map (Dict): The nested dictionary to access.
            path (Tuple[str]): The path sequence of keys to access in
            the dictionary. expected (Union[Dict, int]): The expected
            result for the given path.

        Asserts:
            The output from `access_nested_map` matches the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests `access_nested_map` raises `KeyError` for invalid paths.

        Parameters:
            nested_map (Dict): The nested dictionary to access.
            path (Tuple[str]): The path sequence of keys to access in the
            dictionary. exception (Exception): The expected exception type.

        Asserts:
            `KeyError` is raised when accessing an invalid path
            in `nested_map`.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function.

    This class tests `get_json` for:
    - Correctly returning JSON data from URLs.
    - Ensuring that `requests.get` is called with the correct URL.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests `get_json`'s output and request behavior.

        Parameters:
            test_url (str): The URL to request JSON data from.
            test_payload (Dict): The expected JSON payload from the URL.

        Asserts:
            `get_json` returns the expected payload.
            `requests.get` is called once with the correct URL.
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function.

    This class tests `memoize` to verify that:
    - A method's result is cached and reused on subsequent calls.
    - The decorated method is only called once even if accessed multiple times.
    """

    def test_memoize(self) -> None:
        """Tests the caching behavior of `memoize`.

        This test verifies that `memoize` caches the result of the method after
        the first call, ensuring the method is only executed once.

        Asserts:
            The cached value is reused on subsequent calls.
            The original method is only called once.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
