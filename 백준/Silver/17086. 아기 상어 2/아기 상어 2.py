import sys

from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

# 높이 너비

lst = [list(input().split()) for _ in range(n)]

st = deque([])

for i in range(n):

    for j in range(m):

        if lst[i][j] == '1':

            st.append((i,j,0))

m_k = 0

while st:

    x, y, k = st.popleft()

    # 이동은 인접한 8방향(대각선 포함)이 가능

    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:

        if 0<= x+dx<n and 0<= y+dy<m and lst[x+dx][y+dy] == "0":

            lst[x+dx][y+dy] = k+1

            st.append((x+dx,y+dy,k+1))

        else:

            m_k = max(m_k, k)

print(k)

            