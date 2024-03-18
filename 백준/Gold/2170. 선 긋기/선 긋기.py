# (-1, 000, 000, 000 ≤ x < y ≤ 1, 000, 000, 000)

import sys

input = sys.stdin.readline

n = int(input())

lst = [(0, 0)] * n

for i in range(n):
    a, b = map(int, input().split())
    lst[i] = (a, b)
lst.sort(key=lambda x: x[0])

cnt = 0
start = lst[0][0]
end = lst[0][1]
cnt += abs(end - start)
for i in range(1, len(lst)):
    x, y = lst[i]
    # 시작점, 끝점
    if y > end:
        # 새로운 끝점이 기존 끝점보다 멀리 있다면 시작점 비교
        if end < x:
            # 기존의 끝점이 새로운 시작점보다 뒤에 있다면 새로운 시작
            cnt += abs(y - x)
            start = x
            end = y
        else:
            # 기존의 끝점이 새로운 시작점보다 먼저 있다 -> 연장
            cnt += abs(y - end)
            end = y
print(cnt)
