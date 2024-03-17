import sys

input = sys.stdin.readline

n, m = map(int,input().split())

select = []

pick = [0]*n

def dfs():

    if len(select) == m:

        print(*select)

        return

        

    prev = -1

    for i in range(n):

        

        if not pick[i] and prev != lst[i]:

            prev = lst[i]

            pick[i]=1

            select.append(lst[i])

            dfs()

            select.pop()

            pick[i]=0

lst = list(map(int,input().split()))

lst.sort()

dfs()

# 각 depth마다 prev가 공유되어야 한다...

# 어떻게....? depth내(for문)에서 돌리면 되는듯