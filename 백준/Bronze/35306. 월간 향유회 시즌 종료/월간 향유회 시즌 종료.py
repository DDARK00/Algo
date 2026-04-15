import sys
input=sys.stdin.readline

n,k=map(int,input().split())
if n==1:
    print(1)
    exit()

human=[list(map(int,input().split()))+[i] for i in range(n)]
ans=set()
for i in range(k):
    human.sort(key=lambda x:-x[i])
    if human[0][i]!=human[1][i]:
        ans.add(human[0][-1])
print(len(ans))