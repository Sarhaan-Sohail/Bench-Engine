import pytest
from data.generator import makedata

def testsameparam():
    """Same kind, size, seed"""
    assert makedata('random', 500, 100) == makedata('random', 500, 100)

def testdiffseed():
    """Different seeds -> different output."""
    assert makedata('random', 500, 42) != makedata('random', 500, 99)

def testsorted():
    """Sorted equal to its own sorted version."""
    arr = makedata('sorted', 100, 42)
    assert arr == sorted(arr)

def testreversed():
    """Reversed is strictly descending."""
    arr = makedata('reversed', 100, 42)
    assert all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))

def testfewuniq():
    """Few_unique has at most 4 unique values."""
    arr = makedata('few_unique', 500, 42)
    assert len(set(arr)) <= 4

def testnearlysrt():
    """Nearly_sorted mismatches <= 2 * (size // 100)."""
    sz = 200
    arr = makedata('nearly_sorted', sz, 42)
    diffs = sum(1 for idx, val in enumerate(arr) if val != idx)
    assert diffs <= 2 * (sz // 100)

def testerrkind():
    """Unknown kind raises ValueError."""
    with pytest.raises(ValueError):
        makedata('unknown', 10, 42)
