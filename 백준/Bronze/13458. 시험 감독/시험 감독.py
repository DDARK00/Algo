import sys

import math

input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))

cnt = 0

a, b = map(int,input().split())

for num in lst:

    cnt+=1

    num-=a

    if num>0:

        cnt+=math.ceil(num/b)

print(cnt)