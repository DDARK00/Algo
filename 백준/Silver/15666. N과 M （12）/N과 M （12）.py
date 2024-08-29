import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# n개중 m개

def dfs(k):

    if len(sel) == m:

        print(*sel)

        return

        

    used = -1

    # 정렬돼 있음^^

    for i in range(k,n):

        if used != lst[i]:

            sel.append(lst[i])

            dfs(i)

            sel.pop()

            used = lst[i]

lst = list(map(int, input().split()))

lst.sort()

sel = []

dfs(0)

