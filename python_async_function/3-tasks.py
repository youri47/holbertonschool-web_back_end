
#!/usr/bin/env python3
"""Module for creating asyncio Tasks."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Crée et retourne un asyncio.Task pour wait_random.

    Args:
        max_delay: délai maximum.

    Returns:
        Un objet asyncio.Task.
    """
    return asyncio.ensure_future(wait_random(max_delay))
