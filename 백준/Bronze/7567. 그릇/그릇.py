import sys
input = sys.stdin.readline

s = input().rstrip()
ans = 0
dir = "m"
for c in s:
    if c == dir:
        ans += 5
    else:
        ans += 10
    dir = c

print(ans)