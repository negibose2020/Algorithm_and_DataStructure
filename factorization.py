# 素因数分解
def factorization(n):
    res = []
    for i in range(2,n):
        if i * i > n:break
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            res.append([i,cnt])
    if n != 1:
        res.append([n,1])
    return res
