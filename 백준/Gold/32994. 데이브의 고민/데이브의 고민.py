import sys
input = sys.stdin.readline
n, m = map(int, input().split())

idx = [0, 2, 4, 1, 3]
for i in range(n):
    for j in range(m):
        print((idx[i%5]+j)%5+1, end=" ")
    print()