import sys
input=sys.stdin.readline

n=int(input())
lst=[input().rstrip() for _ in range(n)]
db={}
for i in range(n):
    db[lst[i]]=1
    if lst[i]=='?':
        if i-1>=0:
            x=lst[i-1][-1]
        else:
            x=None
        if i+1<n:
            y=lst[i+1][0]
        else:
            y=None

for _ in range(int(input())):
    target=input().rstrip()
    if not db.get(target) and (target[0]==x or x==None) and (target[-1]==y or y==None):
        print(target)
        break