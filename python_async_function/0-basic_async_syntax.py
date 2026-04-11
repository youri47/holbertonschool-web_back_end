#!/usr/bin/env python3
"""Module for basic async syntax."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Attend un délai aléatoire entre 0 et max_delay, puis le retourne.

    Args:
        max_delay: délai maximum en secondes (défaut: 10).

    Returns:
        Le délai aléatoire effectivement attendu.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
