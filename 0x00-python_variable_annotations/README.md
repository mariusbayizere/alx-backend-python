# Python Type Annotations Project

## Overview

This project demonstrates the use of type annotations in Python to enhance code readability and maintainability. The project includes various tasks that involve writing type-annotated functions and defining variables with specific types.

The code is intended to be run on Ubuntu 18.04 LTS with Python 3.7. All scripts should adhere to the `pycodestyle` guidelines and include appropriate documentation for modules, classes, and functions.

## Requirements

- **Allowed editors**: vi, vim, emacs
- **Python version**: 3.7
- **Operating System**: Ubuntu 18.04 LTS
- **Documentation**: All files must include documentation for modules, classes, and functions.
- **Style**: Follow `pycodestyle` version 2.5.
- **File requirements**: All files must end with a newline and be executable.
- **Line length**: Ensure no line exceeds 79 characters.

## Tasks

### Task 0: Basic Annotations - `add`

- **File**: `0-add.py`
- **Function**: `add(a: float, b: float) -> float`
- **Description**: Takes two floats as arguments and returns their sum as a float.

### Task 1: Basic Annotations - `concat`

- **File**: `1-concat.py`
- **Function**: `concat(str1: str, str2: str) -> str`
- **Description**: Concatenates two strings and returns the result.

### Task 2: Basic Annotations - `floor`

- **File**: `2-floor.py`
- **Function**: `floor(n: float) -> int`
- **Description**: Takes a float as an argument and returns its floor value as an integer.

### Task 3: Basic Annotations - `to_str`

- **File**: `3-to_str.py`
- **Function**: `to_str(n: float) -> str`
- **Description**: Converts a float to its string representation.

### Task 4: Define Variables

- **File**: `4-define_variables.py`
- **Variables**:
  - `a: int = 1`
  - `pi: float = 3.14`
  - `i_understand_annotations: bool = True`
  - `school: str = "Holberton"`

### Task 5: Complex Types - List of Floats

- **File**: `5-sum_list.py`
- **Function**: `sum_list(input_list: List[float]) -> float`
- **Description**: Takes a list of floats and returns their sum as a float.

### Task 6: Complex Types - Mixed List

- **File**: `6-sum_mixed_list.py`
- **Function**: `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`
- **Description**: Takes a list of integers and floats and returns their sum as a float.

### Task 7: Complex Types - String and Int/Float to Tuple

- **File**: `7-to_kv.py`
- **Function**: `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`
- **Description**: Returns a tuple where the first element is a string and the second element is the square of the int/float value.

### Task 8: Complex Types - Functions

- **File**: `8-make_multiplier.py`
- **Function**: `make_multiplier(multiplier: float) -> Callable[[float], float]`
- **Description**: Returns a function that multiplies a float by the given multiplier.

### Task 9: Let's Duck Type an Iterable Object

- **File**: `9-element_length.py`
- **Function**: `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]`
- **Description**: Returns a list of tuples, each containing an iterable and its length.

### Task 10: Duck Typing - First Element of a Sequence

- **File**: `100-safe_first_element.py`
- **Function**: `safe_first_element(lst: Sequence[Any]) -> Union[Any, None]`
- **Description**: Returns the first element of a sequence or `None` if the sequence is empty.

### Task 11: More Involved Type Annotations

- **File**: `101-safely_get_value.py`
- **Function**: `safely_get_value(dct: Mapping, key: Any, default: Optional[Union[T, None]] = None) -> Union[Any, T]`
- **Description**: Returns the value for a key in a dictionary or a default value if the key is not found.

### Task 12: Type Checking

- **File**: `102-type_checking.py`
- **Function**: `zoom_array(lst: Tuple, factor: int = 2) -> List`
- **Description**: Returns a list where each element of the tuple is repeated `factor` times.

## Running the Code

To run the code, ensure that all files are executable:

```sh
chmod +x *.py

