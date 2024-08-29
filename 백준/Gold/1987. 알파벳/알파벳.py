import sys

input = sys.stdin.readline

r, c = map(int,input().split())

# 세로 가로

lst = [input().strip() for _ in range(r)]

# 알파벳

visited = [0]*26

def dfs(x,y,d):

    global m_cnt

    

    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:

        nx = x+dx

        ny = y+dy

        

        if 0<=nx<r and 0<= ny<c :

            alpha = ord(lst[nx][ny]) - 65

            

            if not visited[alpha]:

                visited[alpha] = 1

                m_cnt = max(m_cnt,d+1)

                dfs(nx,ny,d+1)

                visited[alpha] = 0

        

visited[ord(lst[0][0])-65]=1

m_cnt = 1

dfs(0,0,1)

print(m_cnt)
# 시작이 좌상0,0이니까 진행 방향 하나 빼도 될  것 같았는데 오답이래