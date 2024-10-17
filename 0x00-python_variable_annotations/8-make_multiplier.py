#!/usr/bin/env python3
"""This file defines a type-annotated function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by <multiplier>"""
    def func(n: float) -> float:
        """Multiplies a float by a multiplier"""
        return n * multiplier
    return func
