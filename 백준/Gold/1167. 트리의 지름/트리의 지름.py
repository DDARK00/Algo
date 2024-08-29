import sys

from math import inf

input = sys.stdin.readline

n = int(input()) # 정점 수

g = {} # 그래프

for _ in range(n):

    v = list(map(int,input().split()))

    node = v[0]

    # 1 23 45 67 -1 8 3번

    g[node] = []

    for i in range((len(v)-2)//2):

        g[node].append((v[2*i+1],v[2*i+2])) # 노드 비용

def dfs(idx):

    dist = [inf]*(n+1)

    dist[0], dist[idx]=0, 0

    st = [(idx, 0)] # 노드 거리

    while st:

        v, w = st.pop()

        for nv, nw in g[v]:

            if dist[nv]>= w+nw:

                dist[nv] = w+nw

                st.append((nv,w+nw))

    # print(dist)

    return dist.index(max(dist)), max(dist)

m_idx, m_val = dfs(1)

print(max(m_val,dfs(m_idx)[1]))
# 알면 쉽고 모르면 헤메는 트리의 지름
# 그래서 이게 맞나