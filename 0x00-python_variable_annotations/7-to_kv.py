#!/usr/bin/env python3
"""This file defines a type-annotated function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Makes a tuple of the given args"""
    v2: float = v ** 2
    return (k, v2)
