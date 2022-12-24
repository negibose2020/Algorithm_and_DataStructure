def bitmask_brute_force_yield(ls):
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
        yield selected_elm
    #     res.append(selected_elm)
    # return res


A = list(range(1,4))
for bits in bitmask_brute_force_yield(A):
    print(bits)
    for bit in bits:
        print(bit)

"""
[]          # bits
[1]         # bits
1           # bit
[2]         # bits
2           # bit
[1, 2]      # bits
1           # bit
2           # bit
[3]         # bits
3           # bit
[1, 3]      # bits
1           # bit
3           # bit
[2, 3]      # bits
2           # bit
3           # bit
[1, 2, 3]   # bits
1           # bit
2           # bit
3           # bit
"""