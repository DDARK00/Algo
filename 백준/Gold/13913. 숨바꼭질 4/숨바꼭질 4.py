import sys
from collections import deque

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

visited = [-1] * 100002

n, k = map(int, input().split())

visited[n] = n

q = deque([(n, 0)])

find = True

while find and q:
    v, c = q.popleft()
    if v == k:
        find = False
        print(c)
        break
    for d in [1, -1, v]:
        if 0 <= v + d <= 100000 and visited[v + d] == -1:
            visited[v + d] = v

            q.append((v + d, c + 1))
            # print(q)


pointer = k
ans = deque([])
while True:
    val = visited[k]
    ans.appendleft(k)
    if val == k:
        break
    k = val

print(*ans)


