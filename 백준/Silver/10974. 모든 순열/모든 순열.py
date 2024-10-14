
import sys
n=int(sys.stdin.readline())
lst=[i for i in range(1,n+1)]

visited = [0]*(n+1)
sel = []
def dfs():
    if len(sel) == n:
        print(*sel)
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i]=1
            sel.append(i)
            dfs()
            sel.pop()
            visited[i]=0
    

dfs()
