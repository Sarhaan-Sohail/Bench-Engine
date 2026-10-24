# File: sorters/heap.py
from sorters.base import BaseSorter

class HeapSorter(BaseSorter):
    def __init__(self):
        super().__init__('heap')

    def sort(self, arr: list) -> list:
        arr_copy = list(arr)
        n = len(arr_copy)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.siftdown(arr_copy, n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]
            self.swaps += 1
            self.siftdown(arr_copy, i, 0)

        return arr_copy

    def siftdown(self, arr: list, n: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparisons += 1
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            self.comparisons += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.swaps += 1
            self.siftdown(arr, n, largest)
