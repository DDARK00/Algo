import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())

# 제작 제조 서빙
# 토기는 아무때나 만드는데 못만든게 있으면 false
# 드링크 제조는 서빙 m이내 여유가 있을 때
# 1. 서빙타임에 서빙한다
# 2. 서빙타임 임박이면 제조를 한다
# 3. 토기를 만든다
# 막히면 false
tl=deque(list(map(int,input().split())))

ok=True
togi=0
# 100만
mk_q=deque([])
serv_q=deque([])

for i in range(1000001):

    if serv_q and serv_q[0]<i:
        ok=False
        break
    
    if serv_q and serv_q[0]==i:
        serv_q.popleft()
        continue

    while tl and tl[0]-m<=i:
        mk_q.append(tl.popleft()) # 만들어야 할 대기목록

    if mk_q and mk_q[0]-1<i:
        ok=False
        break

    if mk_q and togi>0:
        togi-=1
        serv_q.append(mk_q.popleft())
    else:
        togi+=1

if tl or mk_q or serv_q:
    ok=False
print(["fail","success"][ok])