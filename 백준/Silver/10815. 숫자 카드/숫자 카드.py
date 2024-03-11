import sys

input = sys.stdin.readline

n = int(input())

obj = {}

for i in input().split():

    obj[i] = 1

m = input()

for i in input().split():

    if obj.get(i):

        print(1, end=" ")

    else:

        print(0, end=" ")