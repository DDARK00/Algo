import sys

from collections import deque

n, k = map(int,input().split())

visited = [100001]*100001

q = deque([(n,0)]) # 현재, ㅇㅣ동카운트

visited[n] = 0

cnt = 0 # 도달횟수

while q :

    co,c = q.popleft()

    if co == k:

        cnt+=1

        continue

    for d in [-1,1,co]:

        if 0<=co+d<100001 and visited[co+d]>=c+1:

            visited[co+d] = c+1

            q.append((co+d,c+1))

print(visited[k])

print(cnt)