import sys
input=sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
if sum(lst)%3 !=0:
    print("No")
    exit()

one=lst.count(1)
two=n-one
if one<two:
    print("No")
else:
    print("Yes")