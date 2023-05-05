def Zalgorithm(S):
    N = len(S)
    A = [0]*N
    A[0] = N
    i, j = 1, 0
    while i < N:
        while i+j < N and S[j]==S[i+j]:
            j += 1
        A[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + A[k] < j :
            A[i+k] = A[k]
            k += 1
        i += k
        j -= k
    return A

s=input()
a=Zalgorithm(s)
print(*a)

# pass Library Checker Z Algorithm
# https://judge.yosupo.jp/problem/zalgorithm