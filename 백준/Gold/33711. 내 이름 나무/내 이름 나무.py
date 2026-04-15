import sys
from collections import defaultdict, deque
input=sys.stdin.readline

n, m, k=map(int,input().split())
# 사람수, 관계수, 거리이내
w = int(input())
names = defaultdict(list)
for _ in range(w):
    u, s = input().split()
    names[s].append(int(u))

g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def calc_dist(lst:list):
    visited = {v:(0,v) for v in lst}
    q = deque([(v,0,v)for v in lst])
    while q:
        v, c, origin = q.popleft()
        if c > k:
            return k+1

        for nv in g[v]:
            if nv not in visited: 
                # 미방문
                visited[nv] = (c+1, origin)
                q.append((nv, c+1, origin))
            elif visited[nv][1] != origin:
                # 동일 이름의 다른 origin
                return visited[nv][0] + c + 1
    return k+1

def solve():
    for lst in names.values():
        if len(lst) == 1:
            continue
        if calc_dist(lst) <= k:
            print("POWERFUL CODING JungHwan")
            return
    print("so sad")

solve()