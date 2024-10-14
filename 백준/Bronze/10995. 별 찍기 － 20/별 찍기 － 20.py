import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    i%2 and print(" *"*n)
    i%2==0 and print("* "*n)