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


"""
# 検証用
class RollingHash():
    def __init__(self, S, base = 317, p = None):
        if p == None:
            if len(S) < 6*10**5:
                self.mod = 1<<61-1
            else:
                # self.mod = 10**9+7
                # self.mod = 1900999999
                self.mod = 67280421310721
        else:
            self.mod = p
        self.mod=67280421310721
        self.S = S
        self.N = len(self.S)
        self.base = base
        self.r_hash = 0
        self.poshash = dict()
        self.pow_base = [1]
        self.poshash[0]=0
        for i in range(self.N):
            self.r_hash *= self.base
            self.r_hash += ord(self.S[i])
            self.r_hash %= self.mod
            self.poshash[i+1] = self.r_hash
            self.pow_base.append((self.pow_base[-1] * self.base) % self.mod)
    
    def get(self, l, r):
        res = self.poshash[r] - self.poshash[l]*self.pow_base[r-l]
        res %= self.mod
        return res
    
    def connect(self, h1value, h2value, h2len):
        res = h1value * self.pow_base[h2len] + h2value
        res %= self.mod
        return res


import random
s=[]
N=25
for i in range(N):
    r=random.randint(0,25)
    s.append(chr(97+r))
string="".join(s)

segtree = SegmentTree_with_RollingHash(string)
# print(rh.poshash)
print(string)
for i in range(10):
    print("---")
    ri=random.randint(0,len(s)-3)
    rl=random.randint(0,ri)
    rr=random.randint(ri+1,len(s))
    rc=chr(97+random.randint(0,25))
    s[ri] = rc
    string="".join(s)
    rh=RollingHash(string)
    rhh=rh.get(rl,rr)
    print(segtree.get_charinfo(ri))
    segtree.set_character(ri,rc)
    print(segtree.get_charinfo(ri))
    sgh=segtree.fold(rl,rr)
    print(ri,rc)
    print("".join(s))
    print(string[rl:rr])
    print(rhh,rr-rl,sgh[1],rhh==sgh[0])
"""