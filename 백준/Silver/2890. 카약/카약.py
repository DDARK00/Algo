import sys
input=sys.stdin.readline
r,c=map(int,input().split())

lst=[]
for _ in range(r):
    for idx, c in enumerate(input().rstrip()):
        if c in '123456789':
            lst.append((idx,int(c)))
            break

lst.sort(key=lambda x:-x[0])
before=0
rank=0
ans={}
for i in range(9):
    idx, num=lst[i]
    if idx!=before:
        rank+=1
    ans[num]=rank
    before=idx
for i in range(1,10):
    print(ans.get(i))