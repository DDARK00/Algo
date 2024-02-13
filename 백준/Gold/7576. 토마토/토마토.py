import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
# m칸 n층

tomatos = []
for _ in range(n):
    tomatos.append(list(map(int,input().split())))
#토마토 세팅

init_tomato = []
empty = 0
good = 0
for i in range(n):
    for j in range(m):
        target = tomatos[i][j]
        if target == 1 :
            init_tomato.append((i,j))
            good += 1
        if target == -1 :
            empty += 1
        
# 첫 상태 좌표
days = 0


di = [0,1,0,-1]
dj = [1,0,-1,0]
# 상하좌우


#bfs
q = deque(init_tomato)

tomorrow = []
while q:
    i, j = q.popleft()
    
    #네 방향
    for k in range(4):
        dxi = i+di[k]
        dxj = j+dj[k]

        if 0 <= dxi < n and 0 <= dxj < m :
            if tomatos[dxi][dxj] == 0 :
                tomatos[dxi][dxj] = 1
                good += 1
                tomorrow.append((dxi,dxj))
    if not q:
        # 큐가 비었으면 -> 하루치 끝남, 내일치가 있으면 더해주고 날짜 쁠러쓰
        q.extend(tomorrow)
        tomorrow = []
        days +=1

# print(tomatos)
# print(days)
# print(good)
# print(empty)
t_cnt = m*n - empty
#토마토의 수

'''
2 2
1 -1
-1 1
이게 1일이 아니라 0일이래서 days에서 1 빼줌
'''
if good == t_cnt:
    print(days-1)
else:
    print(-1)
