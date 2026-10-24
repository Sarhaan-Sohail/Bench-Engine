import statistics
from sorters.catalog import displayName


def buildSummary(runRows, countRows):
    groups = {}
    for row in runRows:
        key = (row[0], row[1], row[2])
        if key not in groups:
            groups[key] = []
        groups[key].append(row[5])

    counts = {}
    for row in countRows:
        counts[(row[0], row[1], row[2])] = (row[4], row[5])

    summary = []
    for key in groups:
        times = groups[key]
        summary.append({
            'label': key[0],
            'name': displayName(key[0]),
            'kind': key[1],
            'size': key[2],
            'median': statistics.median(times) * 1000,
            'min': min(times) * 1000,
            'comparisons': counts[key][0],
            'swaps': counts[key][1],
        })
    return summary