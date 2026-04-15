import sys
input=sys.stdin.readline

n,m=map(int,input().split())
cw=['#'*(m+1)]

for _ in range(n):
    cw.append('#'+input().rstrip())

answer=set()
for i in range(n+1):
    for j in range(m+1):
        if cw[i][j]=='#':
            flag=False
            if j+2<m and cw[i][j+1]=='.' and cw[i][j+2]=='.' and cw[i][j+3]=='.':
                answer.add((i,j+1))
            if i+2<n and cw[i+1][j]=='.' and cw[i+2][j]=='.' and cw[i+3][j]=='.':
                answer.add((i+1,j))
print(len(answer))
for i ,j in sorted(answer):
    print(i,j)