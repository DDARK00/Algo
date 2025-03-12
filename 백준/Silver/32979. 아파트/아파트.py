import sys
input=sys.stdin.readline

n=int(input())
t=int(input())
n*=2
apt = list(map(int,input().split()))
b = list(map(int,input().split()))
x = 0
for num in b:
    num-=1
    x = (x+num)%n
    print(apt[x%n])