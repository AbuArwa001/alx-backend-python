#!/usr/bin/env python3
"""
Test module for parameterized test
"""
import unittest
from unittest.mock import patch, Mock, create_autospec
# from functools import lru_cache as memoize
from utils import access_nested_map, get_json, memoize
# import mock
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
    
    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_res = Mock()
        mock_res.json.return_value = test_payload
        mock_get.return_value = mock_res

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property() 
            mock_method.assert_called_once()
