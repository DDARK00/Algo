import sys
input=sys.stdin.readline
a, b = 0, 0
ans ="yes"
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x<a or y<b:
        ans = "no"
    a, b = x, y
print(ans)