#!/usr/bin/env python3
"""
Test module for parameterized test
"""
import unittest
from utils import access_nested_map
# import assertEqual
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)