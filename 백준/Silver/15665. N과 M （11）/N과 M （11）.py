import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# n개중 m개

def dfs():

    if len(sel) == m:

        print(*sel)

        return

        

    used = -1

    # 정렬돼 있음^^

    for i in range(n):

        if used != lst[i]:

            sel.append(lst[i])

            dfs()

            sel.pop()

            used = lst[i]

lst = list(map(int, input().split()))

lst.sort()

sel = []

dfs()

