import sys
input=sys.stdin.readline
n=int(input())

eli=0
money=0
flag=False #
for i in range(n):
    x,p=map(int,input().split())
    if money>x:
        if flag:
            print('Zzz')
            exit()
        else: # 안되면 큰거 제외
            if eli>p and (money-eli)<=x:
                money=money-eli+p
            # 이번거
            flag=True
    else:
        money+=p
        eli=max(eli,p)
print('Kkeo-eok')