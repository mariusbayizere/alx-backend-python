# ALX Backend Python: 0x00. Python - Variable Annotations

## Description
This project is focused on learning and implementing type annotations in Python. Each task involves writing functions with type annotations to ensure type safety and improve code readability.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation
- All your classes should have documentation
- All your functions (inside and outside a class) should have documentation

## Tasks

### 0. Basic annotations - add
Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

**File:** `0-add.py`

### 1. Basic annotations - concat
Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string.

**File:** `1-concat.py`

### 2. Basic annotations - floor
Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.

**File:** `2-floor.py`

### 3. Basic annotations - to string
Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.

**File:** `3-to_str.py`

### 4. Define variables
Define and annotate the following variables with the specified values:
- `a`: an integer with a value of 1
- `pi`: a float with a value of 3.14
- `i_understand_annotations`: a boolean with a value of True
- `school`: a string with a value of “Holberton”

**File:** `4-define_variables.py`

### 5. Complex types - list of floats
Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.

**File:** `5-sum_list.py`

### 6. Complex types - mixed list
Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

**File:** `6-sum_mixed_list.py`

### 7. Complex types - string and int/float to tuple
Write a type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.

**File:** `7-to_kv.py`

### 8. Complex types - functions
Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.

**File:** `8-make_multiplier.py`

### 9. Let's duck type an iterable object
Annotate the below function’s parameters and return values with the appropriate types:
```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
