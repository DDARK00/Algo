import sys, math
input = sys.stdin.readline

n, l = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(n)]
lst.sort()

ans = 0
before = -1
for s, e in lst:
    if e>before:
        s  = max(before, s)
        diff = e - s
        bar = math.ceil(diff/l)
        # print(s, e, diff, bar, before)
        ans += bar
        before = l*bar+s
print(ans)