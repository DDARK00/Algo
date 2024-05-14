import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    lst = [tuple(map(int,input().split())) for _ in range(n)]
    sel = 100001
    lst.sort()
    ans = 0

    for a, b in lst:
        if sel and sel<b:
            # b가 크다-> 뒤떨어진다ㅇ
            continue

        sel = b
        ans+=1
    print(ans)