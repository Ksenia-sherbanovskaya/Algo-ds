"""
Unit tests for 00.Demo
"""

import random
from itertools import pairwise
import pytest
from comp_swap_container import CompSwapList
import sorting_algo


@pytest.fixture(scope="module")
def array_for_bubble():
    r = random.Random()
    r.seed(123456)
    data = list(range(1000))
    r.shuffle(data)
    yield CompSwapList(data)

@pytest.fixture(scope="module")
def array_for_merge():
    r = random.Random()
    r.seed(123456)
    data = list(range(1000))
    r.shuffle(data)
    yield CompSwapList(data)

def test_bubble_sort(array_for_bubble):
    sorting_algo.bubble_sort(array_for_bubble)
    assert all( x <= y for x,y in pairwise(array_for_bubble))
    print("bubble sort -  done")

def test_merge_sort(array_for_merge):
    sorting_algo.merge_sort(array_for_merge)
    assert all( x <= y for x,y in pairwise(array_for_merge))
    print("merge sort -  done")


