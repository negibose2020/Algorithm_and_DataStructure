# 約数を列挙
# 約数列挙
def enumerate_divisors(N):
    res = set()
    for i in range(1,N):
        if i * i > N:break
        if N % i ==0:
            res.add(i)
            res.add(N//i)
    return sorted(res)

"""
# pass アルゴリズムと数学　演習問題集   013 - Divisor Enumeration
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_m

n=int(input())
ans=enumerate_divisors(n)
print(*ans)
"""