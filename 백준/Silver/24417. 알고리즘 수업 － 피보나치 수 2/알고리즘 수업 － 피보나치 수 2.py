import sys
input=sys.stdin.readline
def solve():
    MOD=1000000007
    def fibonacci(n):
        dp=[1,1]
        for i in range(3,n+1):
            dp=[dp[1],(dp[0]+dp[1])%MOD]
        return dp[1]

    n=int(input())
    print(fibonacci(n),n-2)
solve()