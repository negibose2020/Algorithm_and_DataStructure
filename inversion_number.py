# 転倒数
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

    def get_value(self, idx):
        idx += self.size
        return self.node[idx]

    def set_value(self, idx, value):
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


def coordinate_compression(ls):
    sortedls = sorted(set(ls))
    dic = {v:i for i,v in enumerate(sortedls)}
    # return dic
    return list(map(lambda x:dic[x], ls))

def inversion_number(ls):
    inv_num = 0
    segtree = SegmentTree(0,lambda x,y:x+y,[0]*len(ls))
    for idx in range(len(ls)):
        inv_num += idx - segtree.fold(0, ls[idx])
        segtree.update(ls[idx], 1)
        # print(segtree.node[len(segtree.node)//2:],inv_num)
    return inv_num


"""
# pass ABC190 F - Shift and Inversions
# https://atcoder.jp/contests/abc190/tasks/abc190_f
n=int(input())
a=list(map(int,input().split()))
ans=inversion_number(a)
for i in range(n):
    print(ans)
    ans+=n-1-a[i]
    ans-=a[i]
"""