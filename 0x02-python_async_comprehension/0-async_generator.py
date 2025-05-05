#!/usr/bin/env python3
"""
Module for an asynchronous generator
"""

import asyncio
import random
from typing import Generator, AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields 10 random numbers between 0-10
    after waiting 1 second asynchronously each time.
    
    Returns:
        AsyncGenerator yielding random float values
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)