import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
"""
lst.sort()

l = 0
r = n-1

diff = float('inf')
while l<r:
    new_diff = lst[l]+lst[r]
    if abs(new_diff)<diff:
        diff = abs(new_diff)
        ans = (lst[l], lst[r])
    if new_diff>0:
        r-=1
    else:
        l+=1
print(*ans)
"""
lst.sort(key = lambda x:abs(x))
diff = float("inf")
for i in range(n-1):
    new_diff = lst[i]+lst[i+1]
    if diff>abs(new_diff):
        diff = abs(new_diff)
        ans = (lst[i],lst[i+1])
print(min(ans),max(ans))