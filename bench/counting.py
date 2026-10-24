def countops(sorter,data):
    sorter.resetmetrics()
    sorter.sort(data)
    return sorter.comparisons, sorter.swaps