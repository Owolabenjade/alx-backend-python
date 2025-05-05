#!/usr/bin/env python3
"""
Module for asynchronous coroutine that waits for a random delay
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) and waits for a
    random delay between 0 and max_delay seconds and eventually returns it.
    
    Args:
        max_delay (int): Maximum delay in seconds. Defaults to 10.
        
    Returns:
        float: Random delay value between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay