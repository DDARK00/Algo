import sys, math
input=sys.stdin.readline

input()
l=list(map(int,input().split()))
x=list(map(int,input().split()))
ans=0
for i, v in enumerate(input().split()):
    v=int(v.replace(".",""))
    ans +=l[i]-(x[i]*v)//10 if v<10 else (v*l[i])//10-x[i]
print(ans)