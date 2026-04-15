import sys
input=sys.stdin.readline

n=int(input())
chk=[0]*(n+1)

answer=[]
data=[input().split() for _ in range(n)]
'''
3
0 0 1
0 -1 1
-1 -1 0
'''
for i in range(n):
    target=1
    for idx,c in enumerate(data[i]):
        if idx==i and c!='0':
            print(-1)
            exit()

        if c=='0' and idx!=i:
            print(-1)
            exit()

        if c=='-1':
            target+=1
    if target>n or target<1 or chk[target]:
        print(-1)
        exit()
    answer.append(target)
    chk[target]=1

for i in range(n):
    target=answer[i]
    for j in range(n):
        if (target<answer[j] and data[i][j]=='-1') or (target>answer[j] and data[i][j]=='1'):
            print(-1)
            exit()

if len(answer)==n:
    for i in range(n):
        print(answer[i],end=" ")
else:
    print(-1)
