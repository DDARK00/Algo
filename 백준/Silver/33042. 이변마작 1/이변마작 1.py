g  = {}

n  = int(input())
for idx, c in enumerate(input().split()):
    cnt = g.get(c, 0)
    if cnt== 4 :
        print(idx+1)
        exit()
    else:
        g[c] = cnt+1
print(0)