import sys
input=sys.stdin.readline

n,g=input().split()
n=int(n)
k=len(set([input().rstrip() for _ in range(n)]))
if g=="Y":
    print(k//1)
elif g=="F":
    print(k//2)
else: # O
    print(k//3)
