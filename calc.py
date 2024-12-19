import numpy as np

class loc_arith:
    def __init__(self, max):
        self.max = max
        self.cb = np.zeros((self.max, self.max), dtype = np.int64)
        for i in range(self.max):
            k = self.max - i - 2
            num = 2 ** (self.max - i - 1)
            for j in range(self.max - 1, k, -1):
                self.cb[i, j] = num
                num *= 2

    def mul(self, a, b):
        neg = False if (a > 1) else True
        neg = neg if (b > 1) else not neg
        a = self.binSplit(abs(a))
        b = self.binSplit(abs(b))
        if ((a == -1) or (b == -1)):
            return -1
        ret = []
        for n1 in a:
            for n2 in b:
                if (not self.cb[n1, n2] in ret):
                    ret.append(self.cb[n1, n2])
        sum = 0
        for n in ret:
            sum += n
        sum = -sum if (neg) else sum
        return sum
    
    def binSplit(self, a):
        bin = self.cb[self.max - 1]
        x = []
        for i in range(self.max):
            n = bin[i]
            if (n <= a):
                x.append(i)
                a -= n
            if (a == 0):
                break;

        if (a != 0):
            x = -1
        return x
