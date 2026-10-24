from sorters.base import BaseSorter
class MergeSorter(BaseSorter):
    def __init__(self):
        super().__init__('merge')
    
    def sort(self, arr:list) ->list:
        arrcopy = list(arr)
        return self.mergesort(arrcopy)
    
    def mergesort(self,arr:list)->list:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])
        return self.merge(left, right)
    
    def merge(self, left:list, right:list)->list:
        result = []
        i=j=0
        while i < len(left) and j < len(right):
            self.comparisons += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j+= 1
            self.swaps += 1
        result.extend(left[i:])
        result.extend(right[j:])
        self.swaps += (len(left) - i) + (len(right) - j)
        return result
    