import numpy as np
def makedata(kind:str, size:int, seed:int) -> list:
    rng = np.random.default_rng(seed)
    if kind == 'random':
        arr = rng.integers(low = 0,high=100001,size=size)
        return arr.tolist()
    elif kind == 'sorted':
        return list(range(size))
    elif kind == "reversed":
        return list(range(size,0,-1))
    elif kind == 'nearly_sorted':
        arr = np.arange(size)
        nswaps = max(1,size //100)
        for _ in range(nswaps):
            idx1 = rng.integers(0,size)
            idx2 = rng.integers(0,size)
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        return arr.tolist()
    elif kind == 'few_unique':
        choices = [10,20,30,40]
        arr = rng.choice(choices,size = size)
        return arr.tolist()
    else:
        raise ValueError(f"Unknown data distribution kind: {kind}")