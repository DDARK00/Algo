import sys
input=sys.stdin.readline
n=int(input())

for _ in range(n):
    a,b,c=map(int,input().split())
    b-=c
    if a==b:
        print("does not matter")
    elif a<b:
        print("advertise")
    else:
        print("do not advertise")