# 0x03. Unittests and Integration Tests

Unit testing is the process of testing that a particular function returns expected results for different sets of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked. Integration tests will test interactions between every part of your code.

Execute your tests with:
```sh
$ python -m unittest path/to/test_file.py
```
Resources
Read or watch:

unittest — Unit testing framework
unittest.mock — mock object library
How to mock a readonly property with mock?
parameterized
Memoization
Learning Objectives
The difference between unit and integration tests.
Common testing patterns such as mocking, parametrizations, and fixtures.
Requirements
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5)
All your files must be executable
All your modules should have documentation
All your classes should have documentation
All your functions (inside and outside a class) should have documentation
All your functions and coroutines must be type-annotated.
Required Files
utils.py
client.py
fixtures.py
Tasks
### 0. Parameterize a unit test
Familiarize yourself with the utils.access_nested_map function and understand its purpose.
Create a TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to.
Decorate the method with @parameterized.expand to test the function for the following inputs:
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
For each of these inputs, test with assertEqual that the function returns the expected result.
The body of the test method should not be longer than 2 lines.
Repo:

GitHub repository: alx-backend-python
Directory: 0x03-Unittests_and_integration_tests
File: test_utils.py
### 1. Parameterize a unit test (Exceptions)
Implement TestAccessNestedMap.test_access_nested_map_exception.
Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand):
nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
Also, make sure that the exception message is as expected.
Repo:

GitHub repository: alx-backend-python
Directory: 0x03-Unittests_and_integration_tests
File: test_utils.py
### 2. Mock HTTP calls
Familiarize yourself with the utils.get_json function.
Define the TestGetJson(unittest.TestCase) class and implement the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.
Use unittest.mock.patch to patch requests.get. Make sure it returns a Mock object with a json method that returns test_payload which you parametrize alongside the test_url that you will pass to get_json with the following inputs:
test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}
Test that the mocked get method was called exactly once (per input) with test_url as argument.
Test that the output of get_json is equal to test_payload.
Repo:

GitHub repository: alx-backend-python
Directory: 0x03-Unittests_and_integration_tests
File: test_utils.py