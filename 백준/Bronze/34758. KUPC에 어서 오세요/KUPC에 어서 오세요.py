import sys
input=sys.stdin.readline
X,Y=map(int,input().split())
for _ in range(int(input())):
    x,y=map(int,input().split())
    if X==x or Y==y:
        print(0)
    else:
        print(1)