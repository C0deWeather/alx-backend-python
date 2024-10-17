#!/usr/bin/env python3
"""This file defines a type-annotated function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Computes the sum of a mixed list of ints and flaots"""
    sum: float = 0
    for n in mxd_lst:
        sum += n
    return sum
