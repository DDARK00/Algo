import sys

input = sys.stdin.readline
n, m = map(int, input().split())
# n명이 타는데 최종 m

# 0->m은 확정이라 정방향은 신경쓸 필요 x
# 역방향에서 스윕한 거리 왕복이니까 x2

goto = []
for _ in range(n):
    a, b = map(int, input().split())
    if b < a:
        # 큰 경우에만
        goto.append((b, a))
        # 계산하기 편하게 뒤집음

goto.sort(key=lambda x: (x[0], x[1]))
# print(goto)
start = -1
end = -1
cnt = m
for x, y in goto:
    if end < x:
        # end 보다 새로운 시작점이 크다면 새로운 시작
        start = x
        end = y
        cnt += (end - start) * 2
    else:
        # end 보다 새로운 시작점이 작다 -> 연장
        if end < y:
            cnt += (y - end) * 2
            end = y
print(cnt)
