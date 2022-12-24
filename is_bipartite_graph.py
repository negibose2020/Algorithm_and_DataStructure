def is_bipartite_graph(G):
    N = len(G)
    col = [-1]*N
    for i in range(N):
        if col[i] != -1:
            continue
        todo = []
        col[i] = 0
        todo.append(i)
        while todo:
            v = todo.pop()
            for to in G[v]:
                if col[to] == -1:
                    todo.append(to)
                    col[to] = col[v]^1
                    continue
                if col[to] == col[v]:
                    return False
                else:
                    continue
    return True