#!/usr/bin/env python3
"""
Module for async comprehension
"""

from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension
    over the async_generator function.
    
    Returns:
        List of 10 random float values
    """
    return [value async for value in async_generator()]