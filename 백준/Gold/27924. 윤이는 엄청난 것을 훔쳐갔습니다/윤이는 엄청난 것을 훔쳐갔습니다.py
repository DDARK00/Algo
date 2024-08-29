import sys

from collections import deque

input = sys.stdin.readline

n = int(input()) # 정점 수

lst = [[] for _ in range(n)]

for _ in range(n-1):

    a, b = map(int,input().split())

    lst[a-1].append(b-1)

    lst[b-1].append(a-1)

a, b, c = map(int,input().split())

# 도망 추격 추격 노드번호

visited = [[0,-1,-1,-1] for _ in range(n)]

# 리프 노드인가, a,b,c 이동횟수

def bfs(start,idx):

    q = deque([(start,0)])

    visited[start][idx] = 0

    while q:

        

        v, c = q.popleft()

        if len(lst[v]) == 1:

            visited[v][0] = 1

        for nv in lst[v]:

            if visited[nv][idx] == -1:

                visited[nv][idx] = c+1

                q.append((nv,c+1))

        

    

bfs(a-1,1)

bfs(b-1,2)

bfs(c-1,3)

# print(visited)

def ans():

    for q, w, e, r in visited:

        if q:

            if w<e and w<r:

                print("YES")

                return

    print("NO")

    return

ans()