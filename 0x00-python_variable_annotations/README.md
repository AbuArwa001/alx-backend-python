# 0x00. Python - Variable Annotations

## Advanced Python

## Resources
Read or watch:
- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## Learning Objectives
### General
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (use `python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (use `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (use `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks
### 0. Basic annotations - add
Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x00-python_variable_annotations`
- File: `0-add.py`

### 1. Basic annotations - concat
Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x00-python_variable_annotations`
- File: `1-concat.py`

### 2. Basic annotations - floor
Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x00-python_variable_annotations`
- File: `2-floor.py`

### 3. Basic annotations - to string
Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x00-python_variable_annotations`
- File: `3-to_str.py`

### 4. Define variables
Define and annotate the following variables with the specified values:
- `a`, an integer with a value of 1
- `pi`, a float with a value of 3.14
- `i_understand_annotations`, a boolean with a value of True
- `school`, a string with a value of “Holberton”

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x00-python_variable_annotations`
- File: `4-define_variables.py`

### 5. Complex types - list of floats
Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x00-python_variable_annotations`
- File: `5-sum_list.py`

### 6. Complex types - mixed list
Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x00-python_variable_annotations`
- File: `6-sum_mixed_list.py`

### 7. Complex types - string and int/float to tuple
Write a type-annotated function `to_kv` that takes a string `k` and an int or float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x00-python_variable_annotations`
- File: `7-to_kv.py`

### 8. Complex types - functions
Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x00-python_variable_annotations`
- File: `8-make_multiplier.py`

### 9. Let's duck type an iterable object
Annotate the below function’s parameters and return values with the appropriate types:

```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
