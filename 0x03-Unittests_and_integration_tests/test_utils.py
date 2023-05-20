#!/usr/bin/env python3
"""
This module contains the unit tests for utils.py
"""
from parameterized import parameterized
from typing import Mapping, Sequence, Any
import unittest

from utils import access_nested_map


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


if __name__ == '__main__':
    unittest.main()
