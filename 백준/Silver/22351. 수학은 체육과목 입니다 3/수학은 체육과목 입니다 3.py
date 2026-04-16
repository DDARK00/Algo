import sys
sys.setrecursionlimit(10**6)
s=sys.stdin.readline().rstrip()
def solve(i,j):
    x=str(i)
    if j==len(s):return i-1
    for k in range(len(x)):
        if k+j>=len(s)or s[k+j]!=x[k]:
            return
    return solve(i+1,j+len(x))

for a in range(1,2889):
    b=solve(a,0)
    if b:
        print(a,b)
        break