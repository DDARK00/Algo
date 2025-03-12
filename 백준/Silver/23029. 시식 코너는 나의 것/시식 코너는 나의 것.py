import sys
input=sys.stdin.readline

n = int(input())

dish = [int(input()) for _ in range(n)]

ans = [[0,0,0] for _ in range(n)]
# eat half no
ans[0][0] = dish[0]
for i in range(1, n):
    ans[i][0] = ans[i-1][2]+dish[i]
    ans[i][1] = ans[i-1][0]+dish[i]//2
    ans[i][2] = max(ans[i-1])
print(max(ans[-1]))