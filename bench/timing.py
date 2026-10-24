import gc
import time

def timesorter(sorter, data:list, warmups:int, repeats: int) -> list:
    for _ in range(warmups):
        _ =sorter.sort(data)
    
    gc.collect()
    gc.disable()
    
    times = []
    try:
        expectsorted = sorted(data)
        for _ in range(repeats):
            starttime = time.perf_counter()
            sortresult = sorter.sort(data)
            endtime = time.perf_counter()
            times.append(endtime - starttime)
            assert sortresult == expectsorted,f"Algorithm '{sorter.name}' output mismatch validation failure!"
            
    finally:
        gc.enable()
    return times