import sys
input=sys.stdin.readline

q=int(input())
# 10000000
ar = [0]*10000001
ar[1] = 5
ar[2] = 20

for i in range(3, 10000001):
    ar[i] = (ar[i-1]*5)%1000000007
# 4*5*5
# 2468
# 02468
# 02468

for _ in range(q):
    n = int(input())
    print(ar[n])
