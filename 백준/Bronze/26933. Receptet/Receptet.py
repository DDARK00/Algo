import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    h, b, k = map(int,input().split())
    ans += k*(b-h) if h<b else 0
print(ans)