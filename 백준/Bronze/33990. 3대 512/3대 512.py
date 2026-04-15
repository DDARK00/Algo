import sys
input=sys.stdin.readline
ans = -1
for _ in range(int(input())):
    k = sum(map(int, input().split()))
    if k>=512 and abs(512-k)<abs(512-ans):
        ans=k
print(ans)