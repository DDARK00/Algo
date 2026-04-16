import sys
input=sys.stdin.readline

lst=[tuple(map(int,input().split()))for _ in range(int(input()))]

e_lst=[]
l,r=0,0
# 천하통일
for s,e in sorted(lst,key=lambda x:x[0]):
    if s<=r:
        r=max(r,e)
    else:
        e_lst.append((l,r))
        l,r=s,e
e_lst.append((l,r))
# 20만

l,r=0,0
bound=0
for s,e in e_lst:
    if bound<s:
        break
    # 점프 점프x중 긴 것
    bound=max(e+e-s,bound)
    r=e
# 10만
print(r)