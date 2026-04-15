import sys
input=sys.stdin.readline
n,k=map(int,input().split())
dol=list(map(int,input().split()))
ok=[0]*(n)
ok[0]=1
for i in range(n-1):
    for j in range(i+1,n):
        if ok[i] and not ok[j] and (j-i)*(1+abs(dol[i]-dol[j]))<=k:
            ok[j]=1
print(ok[n-1]and"YES"or"NO")