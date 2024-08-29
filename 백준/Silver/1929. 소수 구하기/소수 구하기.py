import sys

input = sys.stdin.readline

n, m =map(int,input().split())

lst = [1]*(m+1)

for i in range(2,int(m**0.5)+1):

    for j in range(2*i,m+1,i):

        lst[j]=0

if n == 1:

    n = 2

for i in range(n,m+1):

    if lst[i]:

        print(i)

# 이게뭐야~~~