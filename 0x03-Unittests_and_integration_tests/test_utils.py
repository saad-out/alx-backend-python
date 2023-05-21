#!/usr/bin/env python3
"""
This module contains the unit tests for utils.py
"""
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Dict,
    Any
)
import unittest
from unittest.mock import patch

import utils
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Class for testing access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
                               self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected_output: Any
                               ) -> None:
        """
        Test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
                               self,
                               nested_map: Mapping,
                               path: Sequence,
                               ) -> None:
        """
        Test access_nested_map function with exception
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Class for testing get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
                      self,
                      test_url: str,
                      test_payload: Dict[str, bool]
                      ) -> None:
        """
        Test get_json function
        """
        with patch("utils.requests.get") as mocked_get:
            mocked_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mocked_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Class for testing memoize function
    """
    def test_memoize(self):
        """
        Test memoize function
        """
        class TestClass:
            """Test Class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()
        with patch.object(TestClass, 'a_method') as mocked_a_method:
            mocked_a_method.return_value = 42
            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)
            mocked_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
