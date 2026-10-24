import random
import pytest

from sorters.cocktailshaker import CocktailShakerSorter
from sorters.heap import HeapSorter
from sorters.insertion import InsertionSorter
from sorters.merge import MergeSorter
from sorters.quick import QuickSorter
from sorters.selection import SelectionSorter

def makeinputs():
    rng = random.Random(42)
    return {
        "empty": [],
        "one_element":[7],
        "two_elements_unsorted":[9,3],
        "all_identical":[4,4,4,4],
        "already_sorted": list(range(1000)),
        "reversed": list(range(1000, 0, -1)),
        "random_seed_42": [rng.randint(-5000, 5000) for _ in range(1000)],
        "negatives_and_duplicates": [-3, 5, -3, 0, 9, -1, 5, 2, -10]
    }
    
def createsorter(label :str):
    if label.startswith('quick_'):
        return QuickSorter(pivot_strat=label.replace('quick_', ''))
    elif label == 'merge':
        return MergeSorter()
    elif label == 'heap':
        return HeapSorter()
    elif label == 'insertion':
        return InsertionSorter()
    elif label == 'selection':
        return SelectionSorter()
    elif label == 'cocktail':
        return CocktailShakerSorter()
    else:
        raise ValueError(f"Unknown sorter label: {label}")

SORTERLABELS = [
    "merge",
    "quick_last",
    "quick_median3",
    "quick_random",
    "heap",
    "insertion",
    "selection",
    "cocktail"
]

INPUTKEYS = [
     "empty",
    "one_element",
    "two_elements_unsorted",
    "all_identical",
    "already_sorted",
    "reversed",
    "random_seed_42",
    "negatives_and_duplicates"
]

@pytest.mark.parametrize('sorterlabel',SORTERLABELS)
@pytest.mark.parametrize('inputkey', INPUTKEYS)
def testsortersagainstinputs(sorterlabel, inputkey):
    sorter = createsorter(sorterlabel)
    testcases = makeinputs()
    orginput = testcases[inputkey]
    inputsnap = list(orginput)
    
    sorter.resetmetrics()
    sortresult = sorter.sort(orginput)
    
    assert sortresult == sorted(inputsnap),f"{sorterlabel}failed to sort {inputkey}"
    assert orginput == inputsnap,f"{sorterlabel}illegally modified the input array structure"
    assert sorter.name == sorterlabel, f"Sorter name mismatch: {sorter.name} != {sorterlabel}"
    if len(orginput) > 1:
        assert (sorter.comparisons + sorter.swaps) > 0, f"{sorterlabel} completed without capturing metrics."
    
def testquicklastreversedlarge():
    """
    Verifies that quick_last on a reversed array of size 5000 
    completes successfully without raising a RecursionError.
    """
    # 1. Create a large reversed array of size 5000
    large_reversed_input = list(range(5000, 0, -1))
    
    # 2. Instantiate quick_last
    sorter = QuickSorter(pivot_strat="last")
    
    # 3. Act & Assert: This will throw a RecursionError if the loop fix isn't applied
    try:
        result = sorter.sort(large_reversed_input)
        assert result == sorted(large_reversed_input)
    except RecursionError:
        pytest.fail("QuickSorter crashed with a RecursionError on size 5000 reversed data!")
