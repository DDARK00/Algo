import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

lst = [tuple(input().rstrip().split(" ")) for _ in range(n)]
q = deque(lst)

while len(q)>1:
    _, idx = q.popleft()
    idx = int(idx)
    q.rotate(-(idx-1)%len(q))
    q.popleft()
print(q[0][0])
# 요세푸스같네