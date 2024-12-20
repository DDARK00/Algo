import sys

input = sys.stdin.readline

n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key=lambda x: (x[0], x[1]))

for l in lst:
    print(*l)
