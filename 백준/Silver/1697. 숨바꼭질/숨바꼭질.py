import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
# 수빈 위치, 동생 위치

# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
#  만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
#  순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 동생은 안 움직이니?

q = deque([(n, 0)])

visited = [0] * 100001

while q:
    coo, cnt = q.popleft()
    if coo == k:
        print(cnt)
        break

    if not visited[coo]:
        visited[coo] = 1
        if coo - 1 >= 0:
            q.append((coo - 1, cnt + 1))
        if coo +1 < 100001:
            q.append((coo + 1, cnt + 1))
        if coo * 2 < 100001:
            q.append((coo * 2, cnt + 1))
