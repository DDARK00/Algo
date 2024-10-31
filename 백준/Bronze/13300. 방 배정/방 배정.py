import sys, math
input=sys.stdin.readline

n, k = map(int, input().split())


g = {
    1:[0, 0],
    2:[0, 0],
    3:[0, 0],
    4:[0, 0],
    5:[0, 0],
    6:[0, 0]
}
for _ in range(n):
    s, y = map(int, input().split())
    # gen01 grad16
    g[y][s] += 1

ans = 0

for i in range(1, 7):
    for j in range(2):
        ans+=math.ceil(g[i][j]/k)
print(ans)