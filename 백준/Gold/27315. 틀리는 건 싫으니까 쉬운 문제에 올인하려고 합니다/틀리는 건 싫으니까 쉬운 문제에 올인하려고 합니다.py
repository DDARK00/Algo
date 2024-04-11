import sys
from math import ceil, inf
from heapq import heappush,heappop
input = sys.stdin.readline
n, m  = map(int,input().split())
# n개중 m개가 몇wa에 가능한가?
lst = []

for _ in range(n):
    d, p, t, e = map(int, input().split())
    # 아이디어 구현 데이터 에디토리얼tf
    # e있으면 그냥 반값행사ㅇ
    if e:
        d, p = ceil(d/2), int(p/2)

    if t:
        p = 0

    # 1순위 쉬운아이디어 쉬운구현ㅇ
    # 2순위는 쉬운아이디어
    # 1솔마다 스텟업 굿
    lst.append((d, p))
hd, hp = map(int,input().split())
# 현재스텟 아이디어, 구현

sol = 0
wa = 0
# 내 아이디어 이하면서 구현은 높은 것들 저장용
pq = []

# 순서 -> 아이디어구현 쉬운거 처치
# 빡구현은 뒤로 미루기 쉬운거부터 하자
# 아이디어 높아서 막히면 아이디어 될 때까지 구현 구르자
# 그러고도 딸리면 런ㅇㅇ
# 남은게 구현밖에 없으면 구르고ㅇ
lst.sort(key = lambda x : (-x[0],-x[1]))
def farming(level):
    global hp # 구현
    global hd # 아이디어
    global wa
    global sol
    while sol<m and pq and level>hd:
        target = heappop(pq)
        wa += target - hp if target>hp else 0
        sol+=1
        hd+=1
        hp+=1

    if level == hd or sol == m:
        return True

    else:
        return False

while sol<m:
    while pq and pq[0]<=hp and sol<m:
        heappop(pq)
        sol+=1
        hp+=1
        hd+=1

    if lst:
        nd,np = lst.pop()
        if nd > hd: # 아이디어 딸리면ㅇ
            if not farming(nd) :# 레벨링
                break

            if sol == m:
                break

        if np>hp: # 구현 딸리면
            heappush(pq,np)

        else: # 날먹가능
            sol+=1
            hp+=1
            hd+=1

    elif pq:
        # 남은 문제가 구현뿐이면
        farming(inf)

    else:
        break

if sol>=m:
    print(wa)

else:
    print(-1)