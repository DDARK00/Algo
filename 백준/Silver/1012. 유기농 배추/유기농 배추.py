import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
# 상하좌우

for _ in range(T):
    # 테케
    m, n, k = map(int,input().split())
    #m호실 n층 k개
    g = {}
    visited = {}
    for _ in range(k):
        a, b = map(int, input().split()) # m n
        # 두 배추의 위치가 같은 경우는 없다.
        g[(a, b)] = []
        visited[(a, b)] = False
        # 방문하지 않음
        for i in range(4):
            if 0 <= a+di[i]<m and 0<= b+dj[i]:
                g[(a, b)].append((a+di[i], b+dj[i]))

    #bfs
    q = deque([])
    # visited = []
    cnt = 0
    for key in g.keys():
        if not visited[key]:
            cnt +=1
            q.append((key))
            
            while q:
                v = q.popleft()
                if g.get(v) and not visited[v]:
                    q.extend(g.get(v))
                    visited[v] = True
    print(cnt)
    # print(visited)
    # 리스트 완탐 돌렸다가 시간초과ㅠ
    # 방문도 딕셔너리