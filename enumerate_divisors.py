# 約数を列挙
def enumerate_divisors(N):
    res = set()
    for i in range(1,N):
        if i * i > N:break
        if N % i ==0:
            res.add(i)
            res.add(N//i)
    return sorted(res)

