import random
from PyQt5.QtCore import QThread, pyqtSignal
from data.generator import makedata
from bench.timing import timesorter
from bench.counting import countops
from bench.config import SLOWMAXSIZE
from sorters.catalog import SLOWLABELS, makeSorter, displayName


class RunWorker(QThread):
    # progress: jobs finished, total jobs, text to show
    progress = pyqtSignal(int, int, str)
    # done: timing rows, count rows
    done = pyqtSignal(list, list)

    def __init__(self, labels, kinds, sizes, warmups, repeats, seed, skipSlow):
        super().__init__()
        self.labels = labels
        self.kinds = kinds
        self.sizes = sizes
        self.warmups = warmups
        self.repeats = repeats
        self.seed = seed
        self.skipSlow = skipSlow
        self.stopRequested = False

    def isSkipped(self, label, size):
        return self.skipSlow and label in SLOWLABELS and size > SLOWMAXSIZE

    def run(self):
        random.seed(self.seed)

        # build the full list of jobs first, so the progress bar knows the total
        jobs = []
        for kind in self.kinds:
            for size in self.sizes:
                for label in self.labels:
                    if not self.isSkipped(label, size):
                        jobs.append((kind, size, label))

        runRows = []
        countRows = []
        for index in range(len(jobs)):
            if self.stopRequested:
                break
            kind, size, label = jobs[index]
            sorter = makeSorter(label)
            data = makedata(kind, size, self.seed)

            self.progress.emit(index, len(jobs),
                               displayName(label) + '   |   ' + kind + '   |   size ' + str(size))

            times = timesorter(sorter, data, self.warmups, self.repeats)
            for i in range(len(times)):
                runRows.append([label, kind, size, self.seed, i, times[i]])

            comparisons, swaps = countops(sorter, data)
            countRows.append([label, kind, size, self.seed, comparisons, swaps])

        if self.stopRequested:
            self.progress.emit(len(runRows) and index or 0, len(jobs), 'Stopped')
        else:
            self.progress.emit(len(jobs), len(jobs), 'Finished')
        self.done.emit(runRows, countRows)