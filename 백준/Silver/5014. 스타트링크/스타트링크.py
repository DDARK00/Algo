import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
if S == G:
    print(0)
    exit()
# F층 중에서
# S에서 출발해서
# G로 가려는데
# 위로 U를 가거나
# 아래로 D를 가거나

#  (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000)
visited = [F+1] * (F+1)
visited[S] = 0
q = deque([(S, 0)])
while q:
    now, cnt = q.popleft()
    for d in (U, -D):
        if 0 < now + d <= F and visited[now + d] > cnt + 1:
            visited[now + d] = cnt + 1
            if now + d == G:
                print(cnt + 1)
                exit()
            q.append((now + d, cnt + 1))
print('use the stairs')

