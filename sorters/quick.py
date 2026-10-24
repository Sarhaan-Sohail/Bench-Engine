import random
from sorters.base import BaseSorter

class QuickSorter(BaseSorter):
    def __init__(self, pivot_strat: str):
        # This properly handles the labels: quick_last, quick_random, quick_median3
        super().__init__(f"quick_{pivot_strat}")
        self.pivot_strat = pivot_strat
    
    def sort(self, arr: list) -> list:
        arrcopy = list(arr)
        self.quicksort(arrcopy, 0, len(arrcopy) - 1)
        return arrcopy
    
    def quicksort(self, arr: list, start: int, end: int):
         while start < end:
            pidx = self.partition(arr, start, end)
            
            # Calculate the sizes of both partitions
            left_size = pidx - start
            right_size = end - pidx
            
            if left_size < right_size:
                # Left side is smaller: Recurse left, then loop right
                self.quicksort(arr, start, pidx - 1)
                start = pidx + 1
            else:
                # Right side is smaller: Recurse right, then loop left
                self.quicksort(arr, pidx + 1, end)
                end = pidx - 1
    
    def partition(self, arr: list, start: int, end: int) -> int:
        if self.pivot_strat == 'last':
            pass
        elif self.pivot_strat == 'random':
            # FIX 1: Swap with 'end' because pivot = arr[end] is used below
            ridx = random.randint(start, end)
            arr[ridx], arr[end] = arr[end], arr[ridx]
            self.swaps += 1
        elif self.pivot_strat == 'median3':
            mid = start + (end - start) // 2
            candidates = [(arr[start], start), (arr[mid], mid), (arr[end], end)]        
            self.comparisons += 3
            candidates.sort(key=lambda x: x[0])
            midx = candidates[1][1]
            arr[midx], arr[end] = arr[end], arr[midx]
            self.swaps += 1
        
        pivot = arr[end]
        i = start - 1
        
        for j in range(start, end):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swaps += 1
        
        # FIX 2: Moved outside the for-loop so it processes the whole subarray
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        self.swaps += 1
        return i + 1
