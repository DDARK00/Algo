import sys
input=sys.stdin.readline

n=int(input())
p=[tuple(map(int, input().split())) for _ in range(n)]
answer=float('inf')
val=float('inf')
def dfs(k,s,b):
    global answer, val
    if k==n:
        answer=min(answer,val)
        return
    ns, nb = p[k]

    val=abs(b+nb - s*ns)
    dfs(k+1,s*ns,b+nb)
    val=abs(b-s)
    dfs(k+1,s,b)

def solve():
    global val
    for i in range(n):
        val=abs(p[i][0]-p[i][1])
        dfs(i+1,*p[i])
solve()
print(answer)