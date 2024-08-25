# 0x03. Unittests and Integration Tests

## Project Overview

This project is focused on creating and running unit tests and integration tests in Python, specifically using `unittest` and `parameterized` modules. The project includes testing various functions, particularly focusing on parameterizing tests, mocking, and testing asynchronous code.

## Requirements

- **Python Version**: The project is developed and tested using Python 3.7 on Ubuntu 18.04 LTS.
- **Pycodestyle**: Ensure that your code follows the PEP 8 style guide. The code is checked using `pycodestyle` version 2.5.
- **Execution**: All Python files must be executable.
- **Shebang**: The first line of all your Python files must be:
  ```python
  #!/usr/bin/env python3
Newline: All files must end with a new line.
Project Structure
Root Directory: The README.md file is located in the root of the project folder.
Required Files:
utils.py: Contains utility functions used across the project.
client.py: Handles client-side operations.
fixtures.py: Provides fixtures for testing.
test_utils.py: Contains unit tests for utils.py.
Documentation
Modules: Every module in this project includes a detailed docstring that describes its purpose.
bash
Copy code
python3 -c 'print(__import__("my_module").__doc__)'
Classes: Each class in this project is documented with its functionality clearly explained.
bash
Copy code
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
Functions: All functions, whether inside or outside a class, have detailed docstrings explaining their purpose and functionality.
bash
Copy code
python3 -c 'print(__import__("my_module").my_function.__doc__)'
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
Type Annotations: All functions and coroutines are type-annotated.
Tasks Overview
0. Parameterize a Unit Test
The objective of this task is to write a parameterized unit test for the utils.access_nested_map function.

Test Class: TestAccessNestedMap
Test Method: test_access_nested_map
Inputs:
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
Expected Outcome: The test should use assertEqual to validate that the function returns the expected result for each input.
Usage
Running Tests: To run the tests, you can use the following command:

bash
Copy code
python3 -m unittest discover
Code Style Check: Ensure that your code conforms to the PEP 8 style guide by running:

bash
Copy code
pycodestyle <file_name>.py
Repository
GitHub Repository: alx-backend-python
Directory: 0x03-Unittests_and_integration_tests
License
This project is licensed under the MIT License - see the LICENSE file for details.
