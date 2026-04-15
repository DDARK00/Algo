import sys
input=sys.stdin.readline

x=int(input())
ans=0
cnt=0
while x>0:
    k=x%10
    if k>4:
        k-=1
    ans+=k*(9**cnt)
    cnt+=1
    x//=10
print(ans)