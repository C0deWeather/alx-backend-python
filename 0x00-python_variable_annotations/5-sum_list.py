#!/usr/bin/env python3
"""This file defines a type-annotated function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculates the sum of a list of floats"""
    sum: float = 0
    for n in input_list:
        sum += n
    return sum
