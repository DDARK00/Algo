import sys

from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())

# n에서 k로 가야됨

visited = [200000]*(100001)

q=deque([(n,0)])

visited[n] = 1

while q:

    now,cnt = q.popleft()

    # print(now)

    if now == k:

        print(cnt)

        break

    for d in [1,-1]:

        if 0<= now+d < 100001 and visited[now+d] >cnt+1:

            visited[now+d] = cnt+1

            q.append((now+d,cnt+1))

    if now+now < 100001 and visited[now+now]>cnt:

        visited[now+now] = cnt

        q.appendleft((now+now,cnt))

