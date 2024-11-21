import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

lst.sort()

val = float('inf')
ans = [0,0,0]
# print(*lst)
for i in range(n-2):
    num = lst[i]
    left = i+1
    right = n-1
    while left < right:
        temp = num+lst[left]+lst[right]
        if val>abs(temp):
            val = abs(temp)
            ans[0], ans[1], ans[2] = num, lst[left], lst[right]
        if temp>0:
            right-=1
        else:
            left+=1
print(*ans)