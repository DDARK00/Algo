import sys
from collections import deque

input = sys.stdin.readline
# deque 를 이용한 테크닉


dq = deque([])

n, l = map(int, input().split())

lst = list(map(int, input().split()))
dq.append((lst[0], 0))  # value 와 idx
print(dq[0][0], end=" ")
# 최솟값 찾기, 맨 앞을 최소로
for i in range(1, n):
    target = lst[i]
    while dq and dq[-1][0] >= target:
        dq.pop()

    dq.append((target, i))
    while dq and dq[0][1] < i - l + 1:
        dq.popleft()
    # print(dq)
    print(dq[0][0], end=" ")
