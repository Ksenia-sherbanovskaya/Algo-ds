"""
Sorting algorithms
"""

from __future__ import annotations
from typing import Any
from comp_swap_container import CompSwapList


def bubble_sort(data: CompSwapList[Any]):
    n = len(data)
    for i in range(n):
        swapped = False 
        for j in range(0,n-i-1):
            if data.less(j+1,j):
                data.swap(j,j+1)
                swapped = True
        if not swapped:
            break

def merge_sort(data: CompSwapList[Any]):
    if len(data)<=1:
        return
    middle = len(data)//2
    left = data[:middle]
    right = data[middle:]
    merge_sort(left)
    merge_sort(right)
    i=j=k=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i+=1
        else:
            data[k] = right[j]
            j+=1
        k+=1
    while i <len(left):
        data[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        data[k] = right[j]
        j+=1
        k+=1