from heapq import heappush, heappop
"""
Graph の受取は、G[u].append((v,dist))
"""
def dijkstra(G, s, t=-1):
    """
    return  :   tuple of (dist_val from s, pre_nodes)
    """
    N = len(G)
    hq = []
    pre_nodes = [-1] * N
    dist = [-1] * N
    seen = [False] * N
    dist[s] = 0
    heappush(hq, (0,s,-1))
    while hq:
        now_dist, now_v, pre_node = heappop(hq)
        if seen[now_v] == True:
            continue

        seen[now_v] = True
        pre_nodes[now_v] = pre_node
        dist[now_v] = now_dist
        if now_v == t:
            return (dist, pre_nodes)
        for to,d in G[now_v]:
            if seen[to] == True:
                continue
            if dist[to]>=0 and now_dist + d >= dist[to]:
                continue
            heappush(hq,(now_dist + d, to, now_v))
    return (dist, pre_nodes)


def restore_path(pre_nodes, s, t):
    path = []
    now = t
    while now != s:
        path.append(now)
        now = pre_nodes[now]
    path.append(s)
    return path[::-1]

"""
### pass Library Checker
### https://judge.yosupo.jp/problem/shortest_path
n,m,s,t=map(int,input().split())
G=[[]for i in range(n)]
for i in range(m):
    u,v,c=map(int,input().split())
    G[u].append((v,c))

d,p=dijkstra(G,s,t)

if d[t]==-1:
    print(-1)
else:
    path=restore_path(p,s,t)
    # print(path)
    print(d[t],len(path)-1)
    for i in range(len(path)-1) :
        print(path[i],path[i+1])
"""