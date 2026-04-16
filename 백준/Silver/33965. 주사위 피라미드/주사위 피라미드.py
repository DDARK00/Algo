import sys
input=sys.stdin.readline

n=int(input())

# 35 35*1
# 70 35*3
# 105 35*6
# 140 35*10
print(int(n*(n+1)/2*35))