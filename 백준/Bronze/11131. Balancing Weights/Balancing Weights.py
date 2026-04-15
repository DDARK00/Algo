import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    s=sum(map(int,input().split()))
    # t=m*d
    # a=t/i
    # 100g ㅁ?ㄹ
    if s ==0:
        ans="Equilibrium"
    elif s>0:
        ans="Right"
    else:
        ans="Left"
    print(ans)