import sys
input=sys.stdin.readline
n,b,c=map(int,input().split())
lst=list(map(int,input().split()))+[0,0]

if b<=c:
    print(sum(lst)*b)
    exit()

# 2 1 2 1 2
# 4 2 1 2 1
# 5 3 2 3 2
# 반례 감사합니다...
ans=0
for i in range(n):
    if lst[i+1]>lst[i+2]:
        # 2개구매 3개구매 1개구매
        k=lst[i+1]-lst[i+2]
        k=min(lst[i],k)
        ans+=k*(b+c)
        lst[i]-=k
        lst[i+1]-=k

        k=min(lst[i],lst[i+1],lst[i+2])
        ans+=k*(b+c+c)
        lst[i]-=k
        lst[i+1]-=k
        lst[i+2]-=k
    else:
        # 3개구매 2개구매 1개구매
        k=min(lst[i],lst[i+1],lst[i+2])
        ans+=k*(b+c+c)
        lst[i]-=k
        lst[i+1]-=k
        lst[i+2]-=k

        k=min(lst[i],lst[i+1])
        ans+=k*(b+c)
        lst[i]-=k
        lst[i+1]-=k
    # 마지막 1개
    ans+=lst[i]*b

# 묶음 구매가 항상 이득?

print(ans)