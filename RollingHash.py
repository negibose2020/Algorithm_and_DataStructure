class RollingHash():
    def __init__(self, S, base = 317, p = 1<<61 -1):
        self.S = S
        self.N = len(self.S)
        self.base = base
        self.mod = p
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
        """
        return  :   hash value of str[l:r)
        """
        res = self.poshash[r] - self.poshash[l]*self.pow_base[r-l]
        res %= self.mod
        return res


# pass ABC141-E Who Says a Pun?
# https://atcoder.jp/contests/abc141/tasks/abc141_e
def f(d):
    dic=dict()
    for i in range(n-d+1):
        h=rh.get(i,i+d)
        if h not in dic:
            dic[h]=[]
        dic[h].append(i)
    # print(dic)
    for k,v in dic.items():
        if min(v)+d <= max(v):
            return True
    return False

n=int(input())
s=input()
rh=RollingHash(s)

ok=0
ng=n
while ng-ok>1:
    mid=(ok+ng)//2
    if f(mid):
        ok=mid
    else:
        ng=mid
print(ok)