import csv
import json
from bench.storage import writeruns, writecounts, writemetadata, RUN_COLUMNS, COUNT_COLUMNS


def testwriteruns(tmp_path):
    path = tmp_path / 'runs.csv'
    rows = [('merge', 'random', 100, 42, 0, 0.001),
            ('merge', 'random', 100, 42, 1, 0.002)]
    writeruns(str(path), rows)
    with open(str(path)) as f:
        data = list(csv.reader(f))
    assert data[0] == RUN_COLUMNS
    assert len(data) == 3


def testwritecounts(tmp_path):
    path = tmp_path / 'counts.csv'
    writecounts(str(path), [('heap', 'sorted', 100, 42, 500, 200)])
    with open(str(path)) as f:
        data = list(csv.reader(f))
    assert data[0] == COUNT_COLUMNS
    assert len(data) == 2


def testwritemetadata(tmp_path):
    path = tmp_path / 'meta.json'
    writemetadata(str(path), {'seed': 42})
    with open(str(path)) as f:
        info = json.load(f)
    assert info['settings']['seed'] == 42
    assert 'python_version' in info