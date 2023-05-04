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
        """
        return  :   hash value of str[l:r)
        """
        res = self.poshash[r] - self.poshash[l]*self.pow_base[r-l]
        res %= self.mod
        return res
    
    def connect(self, h1value, h2value, h2len):
        """
        return  :   hash value of connected string
        """
        res = h1value * self.pow_base[h2len] + h2value
        res %= self.mod
        return res

"""
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
"""

"""
# pass ABC284    F - ABCBAC
# https://atcoder.jp/contests/abc284/tasks/abc284_f

n=int(input())
t=input()
r=t[::-1]
rh_t=RollingHash(t)
rh_r=RollingHash(r)

# t="abcbac"
# r="cabcba"

for i in range(n):
    abc=rh_t.get(0,i)
    abc2=rh_t.get(2*n-n+i,2*n)
    abc=rh_t.connect(abc,abc2,n-i)
    cba=rh_r.get(n-i,n-i+n)
    if abc==cba:
        print(r[n-i:n-i+n])
        print(i)
        exit()
print(-1)

"""