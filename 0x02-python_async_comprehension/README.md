# 0x02. Python - Async Comprehension

## Overview
This project covers asynchronous comprehension in Python, focusing on writing asynchronous generators, using async comprehensions, and type-annotating generators. The tasks require implementing various asynchronous functions and comprehensions.

## Learning Objectives
By the end of this project, you should be able to:
- Write an asynchronous generator.
- Use async comprehensions.
- Type-annotate generators.

## Requirements
- **Editors**: vi, vim, emacs
- **Interpreter**: All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- **Code Style**: Code should follow `pycodestyle` (version 2.5.x).
- **Documentation**: 
  - All modules should have documentation.
  - All functions should have documentation.
  - Documentation should be a real sentence explaining the purpose of the module, class, or method.

## Tasks

### 0. Async Generator
Write a coroutine called `async_generator` that takes no arguments.
- The coroutine will loop 10 times, each time asynchronously waiting 1 second, then yielding a random number between 0 and 10.

**Usage**:
```python
#!/usr/bin/env python3

import asyncio
from random import uniform
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

# Example usage
async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
