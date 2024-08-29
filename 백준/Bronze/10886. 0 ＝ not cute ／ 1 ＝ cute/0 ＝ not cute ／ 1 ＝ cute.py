import sys
input = sys.stdin.readline

n = int(input())

g = {0:0,1:0}
for _ in range(n):
    g[int(input())]+=1
if g[0]<g[1]:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")