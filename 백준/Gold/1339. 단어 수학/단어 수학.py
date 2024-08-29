import sys
input = sys.stdin.readline
n = int(input())

g = {}
for _ in range(n):
    s = input().rstrip()
    for idx, c in enumerate(s):
        lv = 10** (len(s) - idx -1)

        if g.get(c):
            g[c]+= lv

        else:
            g[c] = lv

lst = list(g.items())
lst.sort(key=lambda x:-x[1])
ans = 0
target = 9

for i in range(len(lst)):
    ans += lst[i][1] *target
    target-=1

print(ans)