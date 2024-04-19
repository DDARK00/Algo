import sys

from heapq import heappop, heappush

from collections import defaultdict

from math import inf

input = sys.stdin.readline

n, m, k = map(int, input().split())

# 정점, 간선, 증액 횟수

g = defaultdict(list)

s, d = map(int, input().split())

# 시작 끝

for _ in range(m):

    a, b, weight = map(int, input().split())

    g[a].append((weight, b))

    g[b].append((weight, a))

visited = [[inf] * (n+1) for _ in range(n + 1)]

# 간선 사용 횟수에 따른 최소치

visited[s][0] = 0

# 노드, edge 수 = 비용

pq = [(0, 0, s)] # w, edgecnt, v

min_v = inf

idx = inf

stop = -1

while pq:

    w, c, v = heappop(pq)

    if c>0 and min(visited[v][:c])<w:

        # print(visited[v][:c], v)

        continue # 더 적은 횟수로 올 수 있을 때 - 이게 플래급이구나

    if visited[v][c] < w:

        continue # 기존 횟수의 비용이 작을때

    if c == n: # 루프ㄴㄴ

        continue

    if v == d:

        if min_v>w:

            min_v = w

            idx = c

        continue

    for nw, nv in g[v]:

        if visited[nv][c + 1] > w + nw:

            visited[nv][c + 1] = w + nw

            heappush(pq, (w + nw, c + 1, nv))

candi = []

# 후보군

# 아 이거 시간복잡도 괜찮냐...

for idx, val in enumerate(visited[d]):

    if val != inf:

        candi.append([val, idx])

# 비용. 간선 수

# ans = [0] * (k + 1)

tax = [0] + [int(input()) for _ in range(k)]

# 그럼 여기서 가장 큰 값(간선이 많이 사용된 값)은 최단거리의 값이지?

for ta in tax:

    min_ans = inf

    for i in range(len(candi)):

        candi[i][0] = candi[i][0] + ta*candi[i][1]

        min_ans = min(min_ans, candi[i][0])

    print(min_ans)

        