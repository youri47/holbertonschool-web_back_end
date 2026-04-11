#!/usr/bin/env python3
"""Module for concurrent coroutines."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Lance wait_random n fois en concurrence et retourne les délais triés.

    Args:
        n: nombre de coroutines à lancer.
        max_delay: délai maximum pour chaque appel.

    Returns:
        Liste des délais dans l'ordre croissant (sans utiliser sort()).
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)
    return delays
