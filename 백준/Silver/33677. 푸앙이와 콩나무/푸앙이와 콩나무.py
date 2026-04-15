import sys
from collections import deque
input=sys.stdin.readline
 
n=int(input())
 
visited = [float('inf')]*(n+1)
need_water = [float('inf')]*(n+1)
q = deque([(0,0,0)]) # h, day, water
visited[0]=0
need_water[0]=0
while q:
    h, d, w = q.popleft()
    if need_water[h]<w:
        continue
 
    for nh, nw in [(h+1,w+1), (h*3,w+3), (h**2,w+5)]:
        if 0<nh<=n and visited[nh]>=d+1 and need_water[nh]>nw:
            visited[nh] = d+1
            need_water[nh] = nw
            q.append((nh, d+1, nw))
print(visited[n], need_water[n])