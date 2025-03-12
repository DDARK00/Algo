import sys
input=sys.stdin.readline

n=int(input())

lst=list(map(int, input().split()))

lst.sort()
# print(lst)
val = 1
for num in lst:
    if num>val:
        break
    val+=num
print(val)