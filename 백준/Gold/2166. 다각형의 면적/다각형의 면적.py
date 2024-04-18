import sys

input = sys.stdin.readline

n = int(input())

lst = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    now = i
    nxt = i + 1
    if nxt == n:
        nxt = 0  # 1y  0x
    answer += lst[now][0] * lst[nxt][1] - lst[nxt][0] * lst[now][1]
answer = abs(answer / 2)

print(round(answer, 2))
