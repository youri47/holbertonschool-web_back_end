#!/usr/bin/env python3
"""Module for task_wait_n."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Comme wait_n mais utilise task_wait_random au lieu de wait_random.

    Args:
        n: nombre de tasks à créer.
        max_delay: délai maximum.

    Returns:
        Liste des délais dans l'ordre croissant.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
