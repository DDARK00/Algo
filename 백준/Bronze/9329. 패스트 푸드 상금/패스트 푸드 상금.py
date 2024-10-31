import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    have = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        mv = 1000001
        for j in range(l[i][0]):
            mv = min(have[l[i][j+1]-1], mv)
            
        ans += l[i][-1]*mv
    print(ans)