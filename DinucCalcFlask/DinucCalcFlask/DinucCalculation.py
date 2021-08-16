from Bio.Seq import Seq

class DinucCalculation():
    """
    Calculation of dinucs frq difference in
    two frames.
    """
    def __init__(self, seq):
        self.seq = seq.lower() + seq[0].lower()
        self.dinuc_table: list[list[str, int, int, float, float, float]] = [['aa', 0, 0, 0, 0, 0],
                                                                            ['ac', 0, 0, 0, 0, 0],
                                                                            ['ag', 0, 0, 0, 0, 0],
                                                                            ['at', 0, 0, 0, 0, 0],
                                                                            ['ca', 0, 0, 0, 0, 0],
                                                                            ['cc', 0, 0, 0, 0, 0],
                                                                            ['cg', 0, 0, 0, 0, 0],
                                                                            ['ct', 0, 0, 0, 0, 0],
                                                                            ['ga', 0, 0, 0, 0, 0],
                                                                            ['gc', 0, 0, 0, 0, 0],
                                                                            ['gg', 0, 0, 0, 0, 0],
                                                                            ['gt', 0, 0, 0, 0, 0],
                                                                            ['ta', 0, 0, 0, 0, 0],
                                                                            ['tc', 0, 0, 0, 0, 0],
                                                                            ['tg', 0, 0, 0, 0, 0],
                                                                            ['tt', 0, 0, 0, 0, 0]]
        self.dinuc_frq_diff_sum: float = 0
        self.dinuc_frq_diff: float = 0
        self.dinuc_frq_diff_list = []
        self.calc()

    def calc(self):
        for n in range(0, len(self.seq) - 1):
            dinuc = self.seq[n:n+2]
            for m in range(0, len(self.dinuc_table)):
                if dinuc == self.dinuc_table[m][0] and n % 2 == 0:
                    self.dinuc_table[m][1] += 1
                elif dinuc == self.dinuc_table[m][0] and n % 2 != 0:
                    self.dinuc_table[m][2] += 1
                else:
                    continue

        seq_dinuc_len = (len(self.seq) - 1) / 2
        for n in range(0, len(self.dinuc_table)):
            #self.dinuc_table[n][3] = float('{:.4f}'.format(self.dinuc_table[n][1] / seq_dinuc_len))
            self.dinuc_table[n][3] = round(self.dinuc_table[n][1] / seq_dinuc_len, 4)
            #self.dinuc_table[n][4] = float('{:.4f}'.format(self.dinuc_table[n][2] / seq_dinuc_len))
            self.dinuc_table[n][4] = round(self.dinuc_table[n][2] / seq_dinuc_len, 4)
            self.dinuc_frq_diff_sum += abs(self.dinuc_table[n][3] - self.dinuc_table[n][4])

            self.dinuc_frq_diff = abs(self.dinuc_table[n][3] - self.dinuc_table[n][4])
            #self.dinuc_table[n][5] = float("{:.4f}".format(self.dinuc_frq_diff))
            self.dinuc_table[n][5] = round(self.dinuc_frq_diff, 4)
            self.dinuc_frq_diff_list.append(self.dinuc_frq_diff)
