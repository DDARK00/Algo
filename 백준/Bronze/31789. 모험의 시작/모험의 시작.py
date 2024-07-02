import sys

input = sys.stdin.readline

n = int(input())

x, s = map(int,input().split())

for _ in range(n):

    c, p = map(int,input().split())

    if c<=x and s<p:

        print("YES")

        exit()

print("NO")