import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# m 개중 n 개는 고정

lst = list(map(int, input().split()))

ar = []

# print(lst)
lst.sort()


def dfs():
    if len(ar) == m:
        print(" ".join(ar))

    for i in range(n):
        if str(lst[i]) not in ar:
            ar.append(str(lst[i]))
            dfs()
            ar.pop()


dfs()
