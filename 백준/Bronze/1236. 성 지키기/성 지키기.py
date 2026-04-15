import sys
input=sys.stdin.readline
n, m = map(int, input().split())
x = [1]*n
y = [1]*m
for i in range(n):
    s = input().rstrip()
    for j in range(m):
        if s[j]=="X":
            x[i]=0
            y[j]=0
print(max(sum(x),sum(y)))