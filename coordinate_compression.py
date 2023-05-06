# 座標圧縮
# 座圧
def coordinate_compression(ls):
    sortedls = sorted(set(ls))
    dic = {v:i for i,v in enumerate(sortedls)}
    # return dic
    return list(map(lambda x:dic[x], ls))

a = [0,10,4,405,2,555,50200,340,2,10]

ca=coordinate_compression(a)
print(ca)