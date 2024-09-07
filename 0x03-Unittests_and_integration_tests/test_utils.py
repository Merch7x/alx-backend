#!/usr/bin/env python3
"""Implementing unit test through the
   unittest module
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Tests various method functionalities"""
    @parameterized.expand([
      ({"a": 1}, ("a",), 1),
      ({"a": {"b": 2}}, ("a",), {"b": 2}),
      ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_acccess_nested_map(self, nested_map, path, expected):
        """Test whether path leads to key accurately"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
