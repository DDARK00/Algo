import sys

from collections import deque

input = sys.stdin.readline

n, w, l = map(int,input().split())

# 트럭수 다리길이 하중

lst = list(map(int,input().split()))

# 트럭 체급

q = deque([0]*w)

sums = 0

turn = 0

idx = 0

while True:

    turn+=1

    out = q.popleft()

    sums-= out

    if idx<n and sums+lst[idx]>l:

        q.append(0)

    elif idx<n:

        q.append(lst[idx])

        sums+=lst[idx]

        idx+=1

    

    if idx == n and sums == 0:

        break

print(turn)