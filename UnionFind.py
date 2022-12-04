class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.members = dict()
        self.roots = set(range(n))
        self.graph = [set() for _ in range (self.n)]

    def find(self, x):
        """ return : root of x."""
        if self.parents[x] < 0:
            if x not in self.members:
                self.members[x] = [x]
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        """ return : root of x and/or y. if x and y have different roots, union them. """
        self.graph[x].add(y)
        self.graph[y].add(x)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return x
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.members[x] += self.members.pop(y)
        self.parents[y] = x
        self.roots.discard(y)
        return x

    def is_same(self, x, y):
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
    
    def breakup(self,x):
        """ return : True   """
        members = self.show_group_members(x)
        for member in members:
            self.parents[member] = -1
            self.roots.add(member)
            self.members[member] = [member]
        return True

    def disunite(self,x,y):
        """ return : True , this method is too take time"""
        if not self.is_same(x,y):return True
        pre_nodes = self.show_group_members(x)
        self.breakup(x)
        self.graph[x].discard(y)
        self.graph[y].discard(x)
        seen = set()
        todo = []
        todo.append(x)
        todo.append(y)
        while todo:
            if len(seen)==len(pre_nodes):break
            now = todo.pop()
            for to in list(self.graph[now]):
                if to in seen:continue
                todo.append(to)
                seen.add(to)
                self.unite(now,to)
        return True
    
    def __str__(self):
        print("This instance are ..." )
        # print("(root, [members])")
        elms = sorted(list(self.load_all_group_members().items()))
        for elm in elms:
            print(elm)
        return "  ... end"

n=int(input())
uf=UnionFind(10)
uf.unite(0,2)
uf.unite(1,3)
uf.unite(0,5)
print(uf)