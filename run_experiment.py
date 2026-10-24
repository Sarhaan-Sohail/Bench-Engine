import os
import sys
import random
import datetime

from data.generator import makedata
from bench.timing import timesorter
from bench.counting import countops
from bench.storage import writeruns, writecounts, writemetadata

from sorters.merge import MergeSorter
from sorters.quick import QuickSorter
from sorters.heap import HeapSorter
from sorters.insertion import InsertionSorter
from sorters.selection import SelectionSorter
from sorters.cocktailshaker import CocktailShakerSorter

#sets
SIZES = [100, 500, 1000, 2500, 5000, 10000]
KINDS = ['random', 'sorted', 'reversed', 'nearly_sorted', 'few_unique']
SEED = 42
WARMUPS = 2
REPEATS = 7
SLOWNAMES = ['insertion', 'selection', 'cocktail']
SLOWMAXSIZE = 5000

# for dry run mode
PREFIX = ''
if len(sys.argv) > 1 and sys.argv[1] == 'dry':
    SIZES = [100, 1000]
    PREFIX = 'dry_'

# in random quick sort, if repeat experiment give the exact seed
random.seed(SEED)

# sorter become the label csv
sorters = [
    MergeSorter(),
    QuickSorter('last'),
    QuickSorter('median3'),
    QuickSorter('random'),
    HeapSorter(),
    InsertionSorter(),
    SelectionSorter(),
    CocktailShakerSorter()
]

# run all
# Two empty lists collect the results. Each item is one CSV row.

runrows = []
countrows = []

for kind in KINDS:
    for size in SIZES:
        # make the data once, then give the same data to every sorter
        data = makedata(kind, size, SEED)
        print('kind=' + kind + '  size=' + str(size))

        for sorter in sorters:
            tooslow = sorter.name in SLOWNAMES and size > SLOWMAXSIZE

            if tooslow:
                print('   skipped ' + sorter.name + ' (too slow at this size)')
            else:
                # timing: returns a list of 7 times
                times = timesorter(sorter, data, WARMUPS, REPEATS)
                for i in range(len(times)):
                    runrows.append([sorter.name, kind, size, SEED, i, times[i]])

                
                comparisons, swaps = countops(sorter, data)
                countrows.append([sorter.name, kind, size, SEED, comparisons, swaps])

os.makedirs('results', exist_ok=True)
stamp = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')

writeruns('results/' + PREFIX + 'runs_' + stamp + '.csv', runrows)
writecounts('results/' + PREFIX + 'counts_' + stamp + '.csv', countrows)
writemetadata('results/' + PREFIX + 'meta_' + stamp + '.json', {
    'sizes': SIZES,
    'kinds': KINDS,
    'seed': SEED,
    'warmups': WARMUPS,
    'repeats': REPEATS,
    'slow_names': SLOWNAMES,
    'slow_max_size': SLOWMAXSIZE
})

print('Done. Timing rows: ' + str(len(runrows)) + '  Count rows: ' + str(len(countrows)))
