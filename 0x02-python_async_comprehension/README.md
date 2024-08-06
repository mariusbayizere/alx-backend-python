# Python Async Comprehensions

## Project Overview

This project is focused on understanding and implementing asynchronous programming in Python. It involves writing coroutines, async comprehensions, and measuring runtime for parallel comprehensions using `asyncio`.

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 18.04 LTS, Python 3.7
- **Code Style**: Pycodestyle (version 2.5.x)
- **File Conventions**:
  - All files should end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/env python3`.
  - All modules and functions must have proper documentation.
  - All functions and coroutines must be type-annotated.

## Tasks

### 0. Async Generator

Write a coroutine called `async_generator` that:
- Takes no arguments.
- Loops 10 times.
- Asynchronously waits 1 second each time.
- Yields a random number between 0 and 10.

### 1. Async Comprehensions

Write a coroutine called `async_comprehension` that:
- Takes no arguments.
- Collects 10 random numbers using an async comprehension over `async_generator`.
- Returns the 10 random numbers.

### 2. Run Time for Four Parallel Comprehensions

Write a coroutine called `measure_runtime` that:
- Executes `async_comprehension` four times in parallel using `asyncio.gather`.
- Measures and returns the total runtime.

## Repository Structure

