#!/usr/bin/env python3
"""This file defines a type-annotated function"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Creates a new list"""
    return [(i, len(i)) for i in lst]
