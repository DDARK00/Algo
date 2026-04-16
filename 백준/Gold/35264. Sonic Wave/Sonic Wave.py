import sys
input=sys.stdin.readline

n=int(input())

k=[0,0,0,0]
# 현 위치에서 가능한 것
# 0, -v, +v

cnt=0
ans=[]
for idx, val in enumerate(map(int,input().split())):
    i=idx%4
    if val==k[i]:
        continue
    cnt+=1
    emit=val-k[i]
    k[i]+=emit
    k[(i+2)%4]-=emit
    ans.append([idx+1,abs(emit),1 if emit<0 else 3])
print(cnt)
for x in ans:
    print(*x)