import sys
input=sys.stdin.readline
r, k, m = map(int, input().split())
for _ in range(m//k):
    r=int(r/2)
    if r==0:
        break
print(r)