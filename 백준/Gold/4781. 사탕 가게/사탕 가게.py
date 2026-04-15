import sys
input=sys.stdin.readline
def solve(n, m):
    dp=[0]*(m+1) 
    for i in range(n):
        c, p = input().split()
        c=int(c)
        p=int(float(p)*100+0.1)
        for j in range(p, m+1):
            dp[j]=max(dp[j], dp[j-p]+c)
    print(dp[m])

while True:
    n, m = input().split()
    # 종류 돈
    if n=="0" and m=="0.00":
        break
    solve(int(n), int(float(m)*100+0.1))