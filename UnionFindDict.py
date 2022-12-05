class UnionFindDict():
    def __init__(self, n=None):
        self.parents = dict()
        self.members = dict()
        self.roots = set()
        if n != None:
            for i in range(n):
                self.find(i)

    def find(self,x):
        """ return : root of x."""
        if x not in self.parents:
            self.parents[x] = -1
            self.roots.add(x)
        if self.parents[x] < 0:
            if x not in self.members:
                self.members[x] = [x]
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

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
        return self.members[root]

    def count_roots(self):
        """ return : number of roots. """
        return len(self.roots)

    def get_all_roots(self):
        """ return : roots of this instance. """
        return self.roots

    def load_all_group_members(self):
        """ return : all of this instance. """
        for root in self.roots:
            if root not in self.members:
                self.members[root] = [root]
        return self.members

    def __str__(self):
        print("This instance are ..." )
        # print("(root, [members])")
        elms = sorted(list(self.load_all_group_members().items()))
        for elm in elms:
            print(elm)
        return "  ... end"

uf1 = UnionFindDict()
uf2 = UnionFindDict(10)
