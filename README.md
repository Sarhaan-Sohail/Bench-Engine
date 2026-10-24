# Bench Engine

> A desktop lab for comparing sorting algorithms by measuring how fast they run, how many operations they perform, and how their speed grows as the input gets bigger.

Bench Engine runs eight sorting algorithms on five kinds of input, times them carefully, counts their comparisons and swaps, and shows the results as a live chart and a table. It is built in Python and has a simple desktop window, so you can pick what to test and see the answer without touching the code.

---

## Features

- **8 algorithms** in a two-level menu: Merge, Quick (last pivot, median of three, random pivot), Heap, Insertion, Selection and Cocktail Shaker sort.
- **5 input types:** random, sorted, reversed, nearly sorted and few unique values.
- **Careful timing:** warm-up runs, repeated timed runs, and garbage collection switched off during timing.
- **Operation counts:** comparisons and swaps are counted in a separate pass, so counting never slows the timing.
- **Log-log charts** with a zoom and pan toolbar, one line per algorithm.
- **Sortable results table** with median time, minimum time, comparisons and swaps.
- **Reproducible runs:** a fixed seed and a saved metadata file record exactly how each experiment was run.
- **Automatic tests** that check every sorter against Python's built-in sort.

---

## Screenshots

_Add screenshots here after your first full run, for example `docs/chart.png` and `docs/table.png`._

---

## Project structure

```
Bench Engine/
├── app.py                 # starts the window
├── run_experiment.py      # runs the full experiment from the terminal
├── protocol.md            # the fixed experiment settings
├── sorters/               # the eight sorting algorithms
│   ├── base.py            # shared interface for every sorter
│   ├── catalog.py         # list of algorithms shown in the UI
│   └── ...                # one file per algorithm family
├── data/
│   └── generator.py       # builds the five input types
├── bench/
│   ├── config.py          # shared settings
│   ├── timing.py          # times one sorter
│   ├── counting.py        # counts comparisons and swaps
│   ├── summary.py         # turns raw rows into summary rows
│   └── storage.py         # writes CSV and JSON files
├── ui/                    # window, panels, chart and table
├── tests/                 # automated tests
└── results/               # saved runs (not stored in git)
```

---

## Requirements

- Python 3.10 or newer
- The libraries in `requirements.txt`: NumPy, pandas, Matplotlib, PyQt5 and pytest

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/bench-engine.git
   cd bench-engine
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # macOS / Linux
   ```

3. Install the libraries:

   ```bash
   python -m pip install -r requirements.txt
   ```

---

## Running the app

From the project folder:

```bash
python app.py
```

1. Tick the algorithms you want. Click **Quick Sort** to tick all three of its variants, or open it and pick one.
2. Choose the input types and sizes.
3. Set repeats, warm-ups and the seed if you want to change them.
4. Click **Run benchmark** and watch the progress bar.
5. Read the **Chart** and **Table** tabs. Click **Save results (CSV)** to keep the data.

Results are saved in the `results/` folder.

---

## Running the full experiment

For the official run that matches `protocol.md`, use the terminal script instead of the window:

```bash
python run_experiment.py          # full run, about 15 to 30 minutes
python run_experiment.py dry      # small test run, a few seconds
```

For a fair result, plug the laptop in, use high-performance power mode, and close other apps and browser tabs. Do not touch the computer while it runs.

The full run writes three files to `results/`: a timing file, a counts file and a metadata file.

---

## Running the tests

```bash
python -m pytest -v
```

The tests check that:

- every sorter returns the correct order for empty, single, duplicate, sorted, reversed and random lists
- no sorter changes the list it was given
- the input generator is reproducible and each input type has the right shape
- the CSV and JSON writers produce the right columns and values
- quicksort handles a reversed list of 5000 items without a recursion error

---

## How the timing works

1. The input data is generated once with a fixed seed, so every algorithm gets the same data.
2. Warm-up runs are executed and thrown away.
3. Garbage collection is switched off.
4. Each run is timed with `time.perf_counter()` and checked against Python's `sorted()`.
5. Garbage collection is switched back on.
6. Comparisons and swaps are counted in a separate pass.

---

## Understanding the results

- **Median** is the typical time for one algorithm on one input. It is less affected by a single slow run than the average.
- **Log-log axes** make growth easy to read. A straight line with slope about 1 means linear growth. A slope near 2 means quadratic growth, which is typical for insertion, selection and bubble-style sorts.
- **Comparisons and swaps** show the work an algorithm does, independent of the computer it runs on. They confirm the timing results.

---

## Limitations

- Results depend on the machine, the Python version and what else is running.
- Pure Python adds overhead, so the absolute times are not comparable to C or C++ implementations.
- Each point uses a small number of repeats (7 by default), so small differences should not be over-interpreted.

---

## Roadmap

- Confidence intervals for the median
- Export charts as PNG files from the window
- Add more sorting algorithms, such as bubble sort and Timsort

---

## License

Add a license here, for example MIT. Choose one at https://choosealicense.com.

---

## Author

Built by **Sarhaan Sohail** as a first Python project.