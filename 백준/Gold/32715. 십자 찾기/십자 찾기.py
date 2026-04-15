import sys
input=sys.stdin.readline

n,m=map(int,input().split())
k=int(input())
board=[[0]*(m+2)]
for _ in range(n):
    board.append([0]+list(map(int,input().split()))+[0])
board.append([0]*(m+2))

p_sum=[[[0,0]for _ in range(m+2)]for _ in range(n+2)]
for i in range(1,n+2):
    for j in range(1,m+2):
        p_sum[i][j][0]=p_sum[i-1][j][0]+board[i][j] # ud
        p_sum[i][j][1]=p_sum[i][j-1][1]+board[i][j] # lr

answer=0
for i in range(1+k,1+n-k):
    for j in range(1+k,1+m-k):
        if board[i][j]:
            x,y=p_sum[i][j]
            if x-p_sum[i-k-1][j][0]-1 == k and p_sum[i+k][j][0]-x == k and y-p_sum[i][j-k-1][1]-1==k and p_sum[i][j+k][1]-y==k:
                answer+=1
                # print(i,j)

print(answer)
# print(*p_sum,sep='\n')