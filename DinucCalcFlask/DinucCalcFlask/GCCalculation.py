class GCCalculation(object):
    """
    Calculates GC percentage in sequence.
    """
    def __init__(self, seq):
        self.seq = seq.lower()
        self.gcCount = 0
        self.gccalculation()

    def gccalculation(self):
        gCount = self.seq.count('g')
        cCount = self.seq.count('c')
        self.gcCount = (gCount + cCount) / len(self.seq) * 100


