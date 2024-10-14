import sys
input=sys.stdin.readline
n = int(input())

ans = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    a, b, c = sorted((a,b,c))
    t = 0
    if a==b and b==c:
        t = a*1000+10000
    elif a==b or b==c:
        t = 1000+b*100
    else:
        t = 100*c
    ans = max(t, ans)
print(ans)