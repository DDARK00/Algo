import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int, input().split()))

lst.sort()
before = sum(lst)
a, b, c, d = lst[0],lst[1],lst[-1],lst[-2]

ans = max(before, before-a-b+a*b*2,before-c-d+c*d*2)
print(ans)