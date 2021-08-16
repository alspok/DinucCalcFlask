import math

class DinucData():
    """Generate table of dinuc in two frames count and frequency"""
    def __init__(self, seq):
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
        self.seq: str = (seq + seq[0]).lower()
        self.dinuc_frq_diff_sum: float = 0
        self.dinucTableComplete()

    def dinucCalc(self):
        """dinuc count in two frames"""
        for n in range(len(self.seq) - 1):
            dinuc = self.seq[n:n + 2]
            for m in range(len(self.dinuc_table)):
                if dinuc == self.dinuc_table[m][0] and n % 2 == 0:
                    self.dinuc_table[m][1] += 1
                elif dinuc == self.dinuc_table[m][0] and n % 2 != 0:
                    self.dinuc_table[m][2] += 1
                else:
                    continue

    def dinucFrqCalc(self):
        """dinuc frq calculation in two different frames"""
        for item in self.dinuc_table:
            item[3] = round(item[1] / (len(self.seq) // 2), 4)
            item[4] = round(item[2] / (len(self.seq) // 2), 4)

    def dinucFrqDiffCalc(self):
        """dinuc frq differencies in two frames calculation"""
        for item in self.dinuc_table:
            item[5] = round(abs(item[3] - item[4]), 4)
            #item[5] = round(item[3] - item[4], 4)

    def dinucFrqDiffSumCalc(self):
        """dinuc frq differencies sum calculation"""
        for item in self.dinuc_table:
            self.dinuc_frq_diff_sum += item[5]
        self.dinuc_frq_diff_sum = round(self.dinuc_frq_diff_sum, 4)

    def dinucTableComplete(self):
        """compleate calc of dinuc table"""
        self.dinucCalc()
        self.dinucFrqCalc()
        self.dinucFrqDiffCalc()
        self.dinucFrqDiffSumCalc()
