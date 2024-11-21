import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
val = abs(lst[0]+lst[-1])
ans = [lst[0], lst[n-1]]
# 투포인터
# left = 0
# right = n-1
# while left<right:
    # temp = lst[left]+lst[right]

    # if abs(temp)<val:
        # val = abs(temp)
        # ans[0] = lst[left]
        # ans[1] = lst[right]
    # if 0 < temp:
        # right-=1
    # else:
        # left+=1
# 이분탐색
# for i in range(n-1):
    # left = i+1
    # right = n-1
    
    # while left<=right:
        # mid = (left+right)//2
        # if 0 < lst[mid]+lst[i]:
            # right = mid -1
        # else:
            # left = mid +1
        # if val>abs(lst[i]+lst[mid]):
            # val = abs(lst[i]+lst[mid])
            # ans[0], ans[1] = lst[i], lst[mid]
# print(*ans)
# 정렬
lst.sort(key=lambda x:abs(x))

val = float("inf")
for i in range(n-1):
    l = lst[i]
    r = lst[i+1]
    if val > abs(l+r):
        val = abs(l+r)
        ans = (l, r)
print(min(ans),max(ans))