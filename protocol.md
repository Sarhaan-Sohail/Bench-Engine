# Experiment Protocol

## Settings (fixed before the full run, never changed after it starts)

- Sizes: 100, 500, 1000, 2500, 5000, 10000
- Kinds: random, sorted, reversed, nearly_sorted, few_unique
- Algorithms: merge, quick_last, quick_median3, quick_random, heap, insertion, selection, cocktail
- Slow algorithms (insertion, selection, cocktail) only run up to size 5000
- Seed: 42
- Warm-ups: 2
- Repeats: 7
- Recursion limit: default (1000)
- Machine: plugged in, high-performance power mode, all other apps closed, browser closed
- GC disabled during timing
- Counting runs in a separate pass, never during timing
- Merge sort counts each element written to the result as one swap

## Step 5 notes (recursion fix)

- Applied tail-recursion elimination inside `QuickSorter.quicksort`: it recurses into the smaller partition and loops over the larger one.
- The default recursion limit (1000) is kept, because this caps stack depth at O(log n), so reversed data no longer overflows.
