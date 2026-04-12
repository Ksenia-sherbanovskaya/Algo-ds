#!/usr/bin/env -S python3
"""
Sortings demo
"""

from comp_swap_container import CompSwapList
import sorting_algo
import random

if __name__ == "__main__":
    r = random.Random()
    r.seed(42)

    data1 = list(range(20))
    r.shuffle(data1)
    container1 = CompSwapList(data1)
    sorting_algo.bubble_sort(container1)
    print(f"Bubble sort: {all(container1[i] <= container1[i+1 ] for i in range(len(container1)-1))}")

    r.seed(42)
    data2 = list(range(20))
    r.shuffle(data2)
    container2 = CompSwapList(data2)
    sorting_algo.bubble_sort(container2)
    print(f"Merge sort: {all(container2[i] <= container2[i+1 ] for i in range(len(container2)-1))}")