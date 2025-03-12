import sys
input = sys.stdin.readline

n, m = map(int, input().split())
face = [input().rstrip() for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if face[i][j] == "#":
            continue
        if j+1<m and face[i][j+1]==".":
            ans+=1
        if i+1<n and face[i+1][j]==".":
            ans+=1

print(ans)