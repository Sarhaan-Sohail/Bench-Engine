from sorters.merge import MergeSorter
from sorters.quick import QuickSorter
from sorters.heap import HeapSorter
from sorters.insertion import InsertionSorter
from sorters.selection import SelectionSorter
from sorters.cocktailshaker import CocktailShakerSorter

GROUPS = [
    ('Merge Sort', [('', 'merge')]),
    ('Quick Sort', [
        ('Last pivot', 'quick_last'),
        ('Median of three', 'quick_median3'),
        ('Random pivot', 'quick_random'),
    ]),
    ('Heap Sort', [('', 'heap')]),
    ('Insertion Sort', [('', 'insertion')]),
    ('Selection Sort', [('', 'selection')]),
    ('Cocktail Shaker Sort', [('', 'cocktail')]),
]

# these three are too slow above size 5000 (see bench/config.py)
SLOWLABELS = ['insertion', 'selection', 'cocktail']

ALLLABELS = []
for groupName, options in GROUPS:
    for optionName, optionLabel in options:
        ALLLABELS.append(optionLabel)


def makeSorter(label):
    if label == 'merge':
        return MergeSorter()
    elif label == 'quick_last':
        return QuickSorter('last')
    elif label == 'quick_median3':
        return QuickSorter('median3')
    elif label == 'quick_random':
        return QuickSorter('random')
    elif label == 'heap':
        return HeapSorter()
    elif label == 'insertion':
        return InsertionSorter()
    elif label == 'selection':
        return SelectionSorter()
    elif label == 'cocktail':
        return CocktailShakerSorter()
    else:
        raise ValueError('Unknown algorithm label: ' + label)


def displayName(label):
    for groupName, options in GROUPS:
        for optionName, optionLabel in options:
            if optionLabel == label:
                if optionName == '':
                    return groupName
                return groupName + ' (' + optionName + ')'