def bitmask_brute_force(ls):
    """
    return : [ list, list, ..., list ]
    """
    N = len(ls)
    res = []
    for i in range(2**N):
        bit_pattern = []
        for j in range(N):
            if i >> j & 1 == 1:
                bit_pattern.append(1)
            else:
                bit_pattern.append(0)
        # print(bit_pattern)
        selected_elm = []
        for j in range(N):
            if bit_pattern[j] == 1:
                selected_elm.append(ls[j])
        res.append(selected_elm)
    return res


A = list(range(1,4))
B = bitmask_brute_force(A)
print(B)
"""
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
"""
for b in B:
    print(b)
"""
[]
[1]
[2]
[1, 2]
[3]
[1, 3]
[2, 3]
[1, 2, 3]
[4]
[1, 4]
[2, 4]
[1, 2, 4]
[3, 4]
[1, 3, 4]
[2, 3, 4]
[1, 2, 3, 4]
"""