import sys
input = sys.stdin.readline

l, p = map(int, input().split())
m = l*p
for num in map(int, input().split()):
    print(num-m, end=" ")

