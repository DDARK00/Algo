import sys
n = int(sys.stdin.readline())

for i in range(n):
    ans = " "*(n-i-1)
    ans = ans+("*"+"*"*i*2)
    print(ans)