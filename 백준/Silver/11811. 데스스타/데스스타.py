import sys;input=sys.stdin.readline

n = int(input())
# 1 2 3 1 11

lst = [list(map(int,input().split()))for _ in range(n)]
for i in range(n):
    target=0
    for j in range(n):
        target |= lst[i][j]
    print(target, end=" ")