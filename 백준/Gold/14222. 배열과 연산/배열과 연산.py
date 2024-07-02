import sys
input = sys.stdin.readline

n, k = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

chk = [0]*(n+1)

for i in range(n-1,-1,-1):
    target = lst[i]

    while target<=n and chk[target]:
        target+=k

    # print(target,"<-target",n)

    if target<=n and not chk[target]:
        chk[target]=1
    else:
        print(0)
        exit()
print(1)