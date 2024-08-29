import sys
input=sys.stdin.readline

n, l = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()
end = -1
cnt = 0
for num in lst:
    if num+0.5>end:
        cnt+=1
        end = num-0.5+l
print(cnt)