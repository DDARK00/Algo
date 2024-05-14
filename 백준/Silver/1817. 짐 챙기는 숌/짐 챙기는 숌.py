import sys

input = sys.stdin.readline

n, m = map(int,input().split())

lst = list(map(int,input().split()))

left = 0

box = 0

for i in lst:

    if left-i<0:

        box+=1

        left = m-i

    else:

        left -=i

print(box)