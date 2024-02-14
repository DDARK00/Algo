import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
ar = []


def dfs():
    if len(ar) == m:
        print(" ".join(ar))

    for i in range(n):
        if len(ar)<m:
            ar.append(str(lst[i]))
            dfs()
            ar.pop()


dfs()
