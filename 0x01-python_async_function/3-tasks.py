#!/usr/bin/env python3
"""
Module for creating asyncio.Task objects
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random
    
    Args:
        max_delay (int): Maximum delay in seconds
        
    Returns:
        asyncio.Task: Task object for wait_random
    """
    return asyncio.create_task(wait_random(max_delay))