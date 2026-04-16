import sys, math
input = sys.stdin.readline

n = int(input())

s = input().rstrip()
ans = 0
for i in range(n//2):
    l = s[i]
    r = s[n-i-1]
    if l == "?" and r == "?":
        ans+=26
    elif l == "?" or r == "?":
        ans+=1
    elif l != r:
        ans=0
        break
print(ans)
    