import sys
input=sys.stdin.readline
n=int(input())

# 4N+2
ans=[[" "]*(4*n+2) for _ in range(2*n)]

for i in range(n*2):
    ans[-1-i][i]="*"

k=2*n+1+n
for i in range(1,n+1):
    ans[i-1][k+i]="*"
    ans[i-1][k-i]="*"
    ans[-1-(i-1)][k+i]="*"
    ans[-1-(i-1)][k-i]="*"

for a in ans:
    print("".join(a))