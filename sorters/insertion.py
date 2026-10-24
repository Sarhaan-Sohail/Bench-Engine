from sorters.base import BaseSorter
class InsertionSorter(BaseSorter):
    def __init__(self):
        super().__init__('insertion')
    
    def sort(self,arr:list) -> list:
        arrcopy = list(arr)
        for i in range(1, len(arrcopy)):
            self.insertionsort(arrcopy, i)
        return arrcopy  
    
    def insertionsort(self,arr:list,i:int) -> list:
        curr = arr[i]
        j = i - 1
        while j >= 0:
            self.comparisons += 1
            if arr[j] > curr:
                arr[j + 1] = arr[j]
                self.swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = curr