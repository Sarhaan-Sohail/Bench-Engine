from sorters.base import BaseSorter
class SelectionSorter(BaseSorter):
    def __init__(self):
        super().__init__('selection')
    
    def sort(self,arr:list) -> list:
        arrcopy = list(arr)
        n = len(arrcopy)
        for i in range(n):
            minidx = i
            for j in range(i+1, n):
                self.comparisons += 1
                if arrcopy[j] < arrcopy[minidx]:
                    minidx = j
            if minidx != i:
                arrcopy[i],arrcopy[minidx] = arrcopy[minidx],arrcopy[i]
                self.swaps += 1
        return arrcopy