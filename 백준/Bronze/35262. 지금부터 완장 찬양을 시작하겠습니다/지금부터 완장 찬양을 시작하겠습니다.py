import sys
input=sys.stdin.readline

n,k=map(int,input().split())
p=0
for c in input().rstrip():
    if c=='0':
        p+=1
    else:
        p=0
    if p==k:
        print(0)
        exit()
print(1)