#!/usr/bin/env python3
"""Module for measuring runtime."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Mesure le temps total de wait_n(n, max_delay) et retourne time / n.

    Args:
        n: nombre de coroutines.
        max_delay: délai maximum.

    Returns:
        Temps moyen par coroutine.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
