import sys

input = sys.stdin.readline

a, b, c, d = map(int,input().split())

print(min(a,b,c-a,d-b))