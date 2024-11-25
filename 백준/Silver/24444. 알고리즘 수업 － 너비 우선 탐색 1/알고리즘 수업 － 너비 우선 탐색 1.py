import sys
input=sys.stdin.readline

n, m, r = map(int, input().split())
g = [[] for _ in range(n+1)]

ans = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
visited = [0]*(n+1)
visited[r] = 1
q = {0:r}
pointer = 0
length = 1
c = 0
last_idx = 1
while length>0:
    c+=1
    v = q[pointer]
    pointer+=1
    ans[v] = c
    length-=1

    for num in sorted(g[v]):
        if not visited[num]:
            visited[num] = 1
            length+=1
            q[last_idx] = num
            last_idx+=1

print(*ans[1:],sep='\n')