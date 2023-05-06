class SegmentTree:
    def __init__(self, e, func, ls):
        """
        e       :   単位元
        func    :   演算
        ls      :   配列
        """
        self.e = e
        self.func = func
        self.size = 1
        while self.size < len(ls):
            self.size <<= 1
        self.node = [self.e] * (2*self.size)
        for idx, v in enumerate(ls, self.size):
            self.node[idx] = v
        for idx in range(self.size -1 , 0, -1):
            self.node[idx] = self.func(self.node[idx<<1|0], self.node[idx<<1|1])
    
    def update(self, idx, value):
        idx += self.size
        self.node[idx] = value
        while idx > 1:
            idx >>= 1
            self.node[idx] = self.func(self.node[idx<<1 | 0], self.node[idx<<1 | 1])

    def fold(self, l, r):
        l += self.size
        r += self.size
        val_l = self.e
        val_r = self.e
        while l < r:
            if l & 1:
                val_l = self.func(val_l, self.node[l])
                l += 1
            if r & 1:
                r -= 1
                val_r = self.func(self.node[r], val_r)
            l >>= 1
            r >>= 1
        return self.func(val_l, val_r)


# pass ABC185 F - Range Xor Query
# https://atcoder.jp/contests/abc185/tasks/abc185_f
n,q=map(int,input().split())
a=list(map(int,input().split()))
def fn(x,y):
    return x^y
e=0
st=SegmentTree(e,fn,a)
for i in range(q):
    t,x,y=map(int,input().split())
    if t==1:
        a[x-1]^=y
        st.update(x-1,a[x-1])
    else:
        print(st.fold(x-1,y))