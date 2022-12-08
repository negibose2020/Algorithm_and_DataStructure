class UnionFindDict_anykey():
    def __init__(self, N_or_list=None):
        self.parents = dict()
        self.members = dict()
        self.roots = set()
        self.node_value = dict()
        self.node_key =dict()
        self.node_num_cnt = 0
        if N_or_list != None:
            if isinstance(N_or_list,int):
                for i in range(N_or_list):
                    self.find(i)
            elif isinstance(N_or_list,list):
                for e in N_or_list:
                    self.find(e)

    def find_origin(self,x):
        """ return : root of x."""
        if x not in self.parents:
            self.parents[x] = -1
            self.roots.add(x)
        if self.parents[x] < 0:
            if x not in self.members:
                self.members[x] = [x]
            return x
        else:
            self.parents[x] = self.find_origin(self.parents[x])
            return self.parents[x]

    def find(self,x):
        if x not in self.node_key:
            xx = self.node_num_cnt
            self.node_key[x] = xx   # key -> value
            self.node_value[xx] = x # value -> key
            self.node_num_cnt += 1
        xx = self.node_key[x]
        return self.find_origin(xx)

    def unite(self,x,y):
        """ return : root of x and/or y. if x and y have different roots, union them. """
        x=self.find(x)
        y=self.find(y)
        if x == y:
            return x
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.members[x] += self.members.pop(y)
        self.parents[y] = x
        self.roots.discard(y)
        return x

    def is_same(self,x,y):
        """ return : True if root of x and y, else False. """
        return self.find(x) == self.find(y)

    def measure_group_size(self, x):
        """ return : size of group x. """
        return -self.parents[self.find(x)]

    def show_group_members(self, x):
        """ return : members of group x. """
        root = self.find(x)
        # return self.members[root]
        res = []
        for m in self.members[root]:
            res.append(self.node_value[m])
        return res

    def count_roots(self):
        """ return : number of roots. """
        return len(self.roots)

    def get_all_roots(self):
        """ return : roots of this instance. """
        # return self.roots
        res = []
        for r in self.roots:
            res.append(self.node_value[r])
        return res

    def __str__(self):
        def load_all_group_members():
            """ return : all of this instance. """
            for root in self.roots:
                if root not in self.members:
                    self.members[root] = [root]
            return self.members

        print("This instance are ..." )
        # print("(root, [members])")
        elms = sorted(list(load_all_group_members().items()))
        for elm_key,elm_values in elms:
            res=[]
            for e_v in elm_values:
                res.append(self.node_value[e_v])
            # print(self.node_value[elm_key],elm_values)
            print("{}:{}".format(self.node_value[elm_key], res))
        return "  ... end"

ls = ["Hokkaido","Aomori","Akita","Iwate","Yamagata","Miyagi","Fukushima"]
uf = UnionFindDict_anykey(ls)
uf.unite("Aomori","Akita")
uf.unite("Akita","Iwate")
uf.unite("Iwate","Miyagi")
uf.unite("Miyagi","Yamagata")
uf.unite("Miyagi","Fukushima")
print(uf)
