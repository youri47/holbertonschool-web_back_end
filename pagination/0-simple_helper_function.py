#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): the page number (1-indexed)
        page_size (int): the number of items per page

    Returns:
        tuple: (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
