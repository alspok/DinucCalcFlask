from random import *

class RandomSeq():
    """
    Make random sequence.
    Input: random sequence length, GC percentage.
    Output: random sequence.
    """
    randseq = ''

    def __init__(self, seqlength, gcpercentage):
        self.seqlength = seqlength
        self.gcpercentage = gcpercentage / 100
        self.randseq = []
        self.atnucs = ['a', 't']
        self.gcnucs = ['g', 'c']


    def randSeq(self):
        for i in range(0, self.seqlength):
            rand = random()
            if rand < self.gcpercentage:
                self.randseq += sample(self.gcnucs, 1)
            else:
                self.randseq += sample(self.atnucs, 1)

        return ''.join(map(str, self.randseq))
