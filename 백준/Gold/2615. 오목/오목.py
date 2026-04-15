import sys
input=sys.stdin.readline

board=[input().split() for _ in range(19)]
chk=[[(1,0),(2,0),(3,0),(4,0)],[(0,1),(0,2),(0,3),(0,4)],[(1,1),(2,2),(3,3),(4,4)],[(-1,1),(-2,2),(-3,3),(-4,4)]]
p=[(5,0),(0,5),(5,5),(-5,5)]
q=[(-1,0),(0,-1),(-1,-1),(1,-1)]
for i in range(19):
    for j in range(19):
        # - | / \
        if board[i][j] !="0":
            for idx, d in enumerate(chk):
                if q[idx][0]+i>=0 and q[idx][0]+i<19 and q[idx][1]+j>=0 and q[idx][1]+j<19 and board[i][j]==board[q[idx][0]+i][q[idx][1]+j]:
                    continue

                cnt=0
                for dx, dy in d:
                    if i+dx<19 and i+dx>=0 and j+dy<19 and board[i][j]==board[i+dx][j+dy]:
                        cnt+=1
                    else:
                        break
                if cnt==4:
                    if i+p[idx][0]>=0 and i+p[idx][0]<19 and j+p[idx][1]>=0 and j+p[idx][1]<19 and board[i][j]==board[i+p[idx][0]][j+p[idx][1]]:
                        continue
                    else:
                        print(board[i][j])
                        print(i+1,j+1)
                        exit()
print(0)