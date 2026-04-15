import sys, math
input=sys.stdin.readline
n=int(input())

# 중앙값 idx n+1//2 -1
# 이후의 수는 쓸모x
# 3579 2^1 2^2 last+1

lst=list(map(int,input().split()))
lst.sort()
answer=1
for i in range((n+1)//2):
    answer+=int(math.log2(lst[i]))

print(answer)