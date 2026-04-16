import sys
input=sys.stdin.readline

def solve():
    h,n=map(int,input().split())
    dp=[0]*(h+1)
    dp[0]=float('inf')
    for _ in range(n):
        hi,si=map(int,input().split())
        for i in range(h-hi,-1,-1):
            if dp[i]!=0:
                ni=dp[i]
                if ni>si:
                    ni=si
                if dp[i+hi]<ni:
                    dp[i+hi]=ni
    print(dp[h])
if __name__ == "__main__":
    solve()