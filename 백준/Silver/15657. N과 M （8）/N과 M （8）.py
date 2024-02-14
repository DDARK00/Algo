import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

ar = []


def dfs(k):
    if len(ar) == m:
        print(" ".join(ar))

    if len(ar) < n:

        for i in range(k, n):
            ar.append(str(nums[i]))
            dfs(i)
            ar.pop()


dfs(0)
# 약간 알겠다 조건에 걸리지 않으면 아무것도 안 함 -> 재귀를 더 들어가지 않음 -> 이게 백트래킹이구나!