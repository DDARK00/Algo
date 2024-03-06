import sys

input = sys.stdin.readline

n= int(input())

tree = {}

for i in range(n):

    tree[i]= []

    for idx,v  in enumerate(list(map(int,input().split()))) :

        if v :

            tree[i].append(idx)

            # i에서 idx로 가는 길이 있다

lst = [[0 for _ in range(n)] for _ in range(n)]

# print(tree)

for i in range(n):

    #dfs

    if tree.get(i) is not None:

        

        stack = []

        stack.extend(tree[i])

        

        while stack:

            v = stack.pop()

            if not lst[i][v]:

                lst[i][v] = 1

                if tree.get(v):

                    stack.extend(tree[v])

    print(*lst[i])

        