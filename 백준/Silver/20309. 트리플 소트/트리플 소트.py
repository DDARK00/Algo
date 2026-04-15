import sys
input=sys.stdin.readline
int(input())

for i,n in enumerate(map(int,input().split())):
    if n%2 == i%2:
        print("NO")
        exit()

print("YES")