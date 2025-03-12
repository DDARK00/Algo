import sys
input=sys.stdin.readline

n=int(input())

aar = list(map(int, input().split()))
bar = list(map(int, input().split()))

aar.sort()
bar.sort()

ai, bi = 0, 0
ans = 0

while ai < n and bi < n:
    if aar[ai]==bar[bi]:
        ans+=1
        if ai>bi:
            aar[ai], aar[bi] = aar[bi], aar[ai]
        elif ai<bi:
            bar[ai], bar[bi] = bar[bi], bar[ai]
        ai+=1
        bi+=1
    elif aar[ai]>bar[bi]:
        bi+=1
    else:
        ai+=1
print(ans)
print(*aar)
print(*bar)