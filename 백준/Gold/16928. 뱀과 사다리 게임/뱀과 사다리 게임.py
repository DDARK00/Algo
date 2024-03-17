import sys

from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

board = [0]*101

# 게임판

visited = [101]*101

# 방문체크, 도달한 카운트

for _ in range(n+m):

    a, b = map(int, input().split())

    board[a] = b

# 세팅

# 1->100

# bfs 시작점, 소비한 카운트

q = deque([(1,0)])

while q:

    now, cnt = q.popleft()

    if now == 100:

        print(cnt)

        break

    for i in range(1,7):

        if now+i<101 and visited[now+i]>cnt:

            visited[now+i] = cnt+1

            # 다음거에 미리 쳌

            if board[now+i]:

                q.append((board[now+i],cnt+1))

            else:

                q.append((now+i,cnt+1))

