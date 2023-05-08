def get_prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    i = 2
    while i * i <= n:
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        i += 1
    return [i for i in range(n + 1) if is_prime[i]]

n = int(input())
p = get_prime(n)
print(*p)