#!/usr/bin/env python3
"""
Module for task-based concurrent coroutines
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of all the delays in ascending order.
    
    Args:
        n (int): Number of times to spawn task_wait_random
        max_delay (int): Maximum delay in seconds
        
    Returns:
        List[float]: List of all delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)