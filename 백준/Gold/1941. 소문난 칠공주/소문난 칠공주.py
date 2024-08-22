import sys
from collections import deque
input = sys.stdin.readline

lst = [input().rstrip() for _ in range(5)]

g = {"Y":0, "S":0}

sel = []
cnt = 0



def chk():
    global cnt
    st = [sel[0]]
    v_cnt = 1
    visit = [0]*7
    visit[0] = 1
    while st :
        x, y = st.pop()
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx, ny = dx + x, dy + y
            try:
                idx = sel.index((nx,ny))
            except Exception:
                idx = -1

            if idx != -1 and not visit[idx]:
                visit[idx] = 1
                v_cnt +=1
                st.append((nx,ny))

    if v_cnt == 7:
        cnt+=1

def dfs(k, c):
    if g["Y"] > 3:
        return

    if c == 7 :
        chk()
        return
    limit = min(25,k+6)
    for j in range(k+1,limit):
        g[lst[j//5][j%5]] += 1
        sel.append((j//5,j%5))
        dfs(j,c+1)
        sel.pop()
        g[lst[j//5][j%5]] -= 1

for i in range(19):
    g[lst[i//5][i%5]] += 1
    sel.append((i//5,i%5))
    dfs(i, 1)
    sel.pop()
    g[lst[i//5][i%5]] -= 1

print(cnt)