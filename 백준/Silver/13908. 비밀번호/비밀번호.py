import sys
input=sys.stdin.readline

n, m = map(int, input().split())
chk=[0]*10
if m>0:
    for k in map(int, input().split()):
        chk[k] = 1

answer = 0
def solve(k,l):
    global answer
    if k==n:
        if l==m:
            answer+=1
        return
    for i in range(10):
        if chk[i]:
            chk[i]=0
            solve(k+1,l+1)
            chk[i]=1
        else:
            solve(k+1,l)
solve(0,0)
print(answer)