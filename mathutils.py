"""Tiny math helpers for the cow-shed P2-B fixture.

Fictional example code used only to exercise the P2-B construction loop.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def clamp(value, low, high):
    """Return value limited to the inclusive range from low to high."""
    if low > high:
        raise ValueError("low must not exceed high")
    if value < low:
        return low
    if value > high:
        return high
    return value
