import sys

input = sys.stdin.readline

n = int(input())


def dfs(k, subset):
    global purm

    if k == n:
        purm.add(subset)
        return

    dfs(k + 1, subset + nums[k])
    dfs(k + 1, subset)


# 부분집합


nums = [*map(int, input().split())]

purm = set()

dfs(0, 0)
# print(purm)
for i in range(1, 100000000):
    if i not in purm:
        print(i)
        break
