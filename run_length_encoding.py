def run_length_encoding(S):
    res = []
    temp = 1
    for i in range (len(S)-1):
        if S[i] == S[i+1]:
            temp += 1
        else:
            res.append([S[i],temp])
            temp = 1
    else:
        if temp > 1:
            res.append([S[i],temp])
        else:
            res.append([S[-1],1])
    return res


a = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
ls = run_length_encoding(a)
print(ls)
# [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
s = "abbcccddd"
ls = run_length_encoding(s)
print(ls)
# [['a', 1], ['b', 2], ['c', 3], ['d', 3]]
