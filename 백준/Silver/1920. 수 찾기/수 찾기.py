import sys

input = sys.stdin.readline

n=input()

counting = {}

# 2(^-31) = -2147483648

# int안박는게 낫지...?

lst = list(input().split())

for i in lst:

    counting[i] = 1

m = input()

mlist = list(input().split())

for j in mlist:

    if counting.get(j):

        print(1)

    else:

        print(0)