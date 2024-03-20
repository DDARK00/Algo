import sys

input = sys.stdin.readline


def dfs(st, sub, select_cnt):
    # 완탐
    global cnt

    if n == st:
        if k == sub and select_cnt > 0:
            cnt += 1

        return

    dfs(st + 1, sub + nums[st], select_cnt + 1)
    dfs(st + 1, sub, select_cnt)


n, k = map(int, input().split())
# n개 중에서 최소 1개 이상 선택하여 합이 k가 되는 경우의 수

nums = [*map(int, input().split())]

used = [0] * n
cnt = 0
dfs(0, 0, 0)

print(cnt)