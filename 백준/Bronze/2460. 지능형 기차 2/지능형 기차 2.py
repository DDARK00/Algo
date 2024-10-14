import sys
input = sys.stdin.readline

z = 0
ans = 0
for _ in range(10):
    a, b = map(int, input().split())
    z-=a
    z+=b
    ans = max(ans, z)
print(ans)