import csv
import json
import platform
import sys
import datetime
import numpy as np

RUN_COLUMNS = ['algorithm', 'kind', 'size', 'seed', 'run_index', 'time_seconds']
COUNT_COLUMNS = ['algorithm', 'kind', 'size', 'seed', 'comparisons', 'swaps']


def writeruns(path, rows):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(RUN_COLUMNS)
        writer.writerows(rows)


def writecounts(path, rows):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(COUNT_COLUMNS)
        writer.writerows(rows)


def writemetadata(path, settings):
    info = {
        'python_version': sys.version,
        'numpy_version': np.__version__,
        'os': platform.platform(),
        'cpu': platform.processor(),
        'date': datetime.datetime.now().isoformat(),
        'settings': settings
    }
    with open(path, 'w') as f:
        json.dump(info, f, indent=2)