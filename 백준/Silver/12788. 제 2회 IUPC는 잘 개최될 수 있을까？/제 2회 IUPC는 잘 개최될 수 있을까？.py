import sys
input = sys.stdin.readline

n = int(input())
m, k = map(int, input().split())

a = list(map(int, input().split()))

a.sort(reverse=True)

minus = m*k
plus = sum(a)

if minus>plus:
    print("STRESS")
else:
    ans = 0
    while minus>0:
        minus -= a[ans]
        ans+=1
    print(ans)