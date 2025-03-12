import sys
from collections import defaultdict
from heapq import heappop, heappush
input=sys.stdin.readline
n, m = 0, 0
def solve():
    # init
    s, d = map(int, input().split())
    g = defaultdict(list)
    for _ in range( m):
        u, v, p = map(int, input().split())
        g[u].append((p, v)) # w, v

    route = [[]for _ in range(n)] # from - to
    route[s] = [s] # tracking loop break
    dist = [float('inf')]*n
    dist[s] = 0

    # solve
    dijk_before(s, g, dist, route)

    if dist[d] == float('inf'):
        print(-1)
        return

    banned = defaultdict(list)
    tracking(s, d, route, banned)
    dist = [float('inf')]*n
    dist[s] = 0
    dijk_after(s, g, dist, banned)
    if dist[d] == float('inf'):
        print(-1)
    else:
        print(dist[d])

def dijk_before(start, g, dist, route):
    pq = [(0,start)]
    while pq:
        w, v = heappop(pq)
        if dist[v] > w:
            continue
        for nw, nv in g[v]:
            if dist[nv]>nw+w:
                heappush(pq, (nw+w, nv))
                dist[nv] = nw+w
                route[nv] = [v]
            elif dist[nv] == nw+w:
                route[nv].append(v)

def tracking(s, e, route, banned):
    st = [e]
    visited = [0]*n

    # u->v is unique
    while st:
        v = st.pop()
        if not visited[v]:
            visited[v]=1
            for bv in route[v]:
                st.append(bv)
                # visited[bv]=1
                banned[bv].append(v) # pk

def dijk_after(s, g, dist, banned):
    pq = [(0, s)]
    while pq:
        w, v = heappop(pq)
        if dist[v] > w:
            continue
        ban = banned.get(v, [])
        for nw, nv in g[v]:
            if nv in ban:
                continue
            if dist[nv] > w+nw:
                dist[nv] = w+nw
                heappush(pq, (w+nw, nv))

while True:
    n, m = map(int, input().split())
    if n==0 and m==0:
        break
    solve()