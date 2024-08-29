import sys

from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

#n까지 k번

q=deque([(0,0)])

visited = [0]*(n+1)

find = False

while q:

    v, c = q.popleft()

    # if c>k:

        # continue

    for delta in[1,int(v/2)]:

        if c+1 <=k:

            if v+delta< n and not visited[v+delta]:

                visited[v+delta] = 1

                q.append((v+delta,c+1))

            elif v+delta == n:

                find = True

                break

if find:

    print("minigimbob")

else:

    print("water")