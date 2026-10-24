from sorters.base import BaseSorter

class CocktailShakerSorter(BaseSorter):
    def __init__(self):
        super().__init__('cocktail')

    def sort(self, arr: list) -> list:
        arr_copy = list(arr)
        n = len(arr_copy)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False
            # Forward pass (like traditional bubble sort)
            for i in range(start, end):
                self.comparisons += 1
                if arr_copy[i] > arr_copy[i + 1]:
                    arr_copy[i], arr_copy[i + 1] = arr_copy[i + 1], arr_copy[i]
                    self.swaps += 1
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            # Backward pass
            for i in range(end - 1, start - 1, -1):
                self.comparisons += 1
                if arr_copy[i] > arr_copy[i + 1]:
                    arr_copy[i], arr_copy[i + 1] = arr_copy[i + 1], arr_copy[i]
                    self.swaps += 1
                    swapped = True

            start += 1

        return arr_copy
