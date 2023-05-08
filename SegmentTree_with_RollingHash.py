class SegmentTree_with_RollingHash:
    def func(self, x, xlen, y, ylen):
        res = x * self.pow_base[ylen] + y
        res %= self.mod
        return [res, xlen + ylen]

    def __init__(self, string):
        # self.mod = 10**9+7
        # self.mod = 1900999999
        self.mod = 67280421310721
        self.base = 317
        self.pow_base = [1]
        self.e = 0
        self.func = self.func
        self.size = 1
        while self.size < len(string):
            self.size <<= 1
        self.node = [[self.e, 0] for i in range(2*self.size)]
        for idx in range(self.size):
            r_hash = 0
            if idx < len(string):
                r_hash += ord(string[idx])
                r_hash %= self.mod
                self.node[idx+self.size] = [r_hash, 1]
            else:
                self.node[idx+self.size] = [0, 0]
            self.pow_base.append((self.pow_base[-1]*self.base) % self.mod)

        for idx in range(self.size -1 , 0, -1):
            self.node[idx] = self.func(self.node[idx<<1|0][0], self.node[idx<<1|0][1] , self.node[idx<<1|1][0], self.node[idx<<1|1][1])

    def get_charinfo(self, idx):
        idx += self.size
        return self.node[idx]

    def set_character(self, idx, c, len = 1):
        idx += self.size
        self.node[idx] = [ord(c) , len]
        while idx > 1:
            idx >>= 1
            self.node[idx] = self.func(self.node[idx<<1 | 0][0], self.node[idx<<1 | 0][1], self.node[idx<<1 | 1][0], self.node[idx<<1 | 1][1])

    def fold(self, l, r):
        l += self.size
        r += self.size
        val_l = [self.e, 0]
        val_r = [self.e, 0]
        while l < r:
            if l & 1:
                val_l = self.func(val_l[0], val_l[1], self.node[l][0],self.node[l][1])
                l += 1
            if r & 1:
                r -= 1
                val_r = self.func(self.node[r][0],self.node[r][1], val_r[0],val_r[1])
            l >>= 1
            r >>= 1
        return self.func(val_l[0],val_l[1], val_r[0],val_r[1])



