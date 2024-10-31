import sys
input=sys.stdin.readline
ans = [0, 1, 2, 3]
for _ in range(int(input())):
    a, b = map(int,input().split())
    ans[a], ans[b] = ans[b], ans[a]
print(ans.index(1))