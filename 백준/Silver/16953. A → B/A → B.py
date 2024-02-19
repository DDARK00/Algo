import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.

q = deque([(a, 0)])
visited = {}

finds = False
while q:
    va, vc = q.popleft()

    if va < b and not visited.get(va):
        visited[va] = 1
        q.extend([(va * 2, vc + 1), (int(str(va) + '1'), vc + 1)])
    elif va == b:
        finds = True
        # print(va, vc)
        break
if finds:
    print(vc+1)
else:
    print(-1)
