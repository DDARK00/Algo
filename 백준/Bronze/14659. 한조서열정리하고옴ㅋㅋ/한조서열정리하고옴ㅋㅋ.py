import sys

input = sys.stdin.readline

n = int(input())
# 활잡이 수
lst = list(map(int, input().split()))

k = -1
mx_cnt = 0
now_cnt = 0
for human in lst:
    if k <= human:
        k = human
        mx_cnt = max(mx_cnt, now_cnt)
        now_cnt = 0
    else:
        now_cnt += 1
mx_cnt = max(now_cnt, mx_cnt)
print(mx_cnt)
