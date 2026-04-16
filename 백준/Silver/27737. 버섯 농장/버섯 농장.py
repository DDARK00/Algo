import sys,math
input=sys.stdin.readline
n,m,k=map(int,input().split())

lst=[input().split() for _ in range(n)]

st=[]
spore=0
for i in range(n):
    for j in range(n):
        if lst[i][j]=='0':
            st.append((i,j))
            cnt=1
            lst[i][j]='1'
            while st:
                x,y=st.pop()
                for nx,ny in [(1+x,y),(-1+x,y),(x,1+y),(x,-1+y)]:
                    if 0<=nx<n and 0<=ny<n and lst[nx][ny]=='0':
                        cnt+=1
                        lst[nx][ny]='1'
                        st.append((nx,ny))
            spore+=math.ceil(cnt/k)

if spore>0 and m>=spore:
    print('POSSIBLE')
    print(m-spore)
else:
    print('IMPOSSIBLE')