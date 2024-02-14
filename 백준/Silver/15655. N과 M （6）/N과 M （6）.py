import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
ar = []


def dfs(k):
    if len(ar) == m:
        print(" ".join(ar))

    for i in range(k, n):
        if str(lst[i]) not in ar:
            ar.append(str(lst[i]))
            dfs(i + 1)
            ar.pop()


dfs(0)
