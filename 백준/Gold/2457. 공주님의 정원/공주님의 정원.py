import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())

lst = [tuple(map(int, input().split())) for _ in range(n)]

lst.sort(key = lambda x : ((x[0],x[1]), (x[2],x[3])))

start_month = 3
start_day = 1

ans = 0
comp = True
pq = []

for sx, sy, ex, ey in lst:
    if start_month == 12:
        break

    if sx > start_month or ( sx == start_month and sy > start_day):
        # print(sx, sy, ans)
        if pq:
            nx, ny = heappop(pq)
            start_month = -nx
            start_day = -ny
            ans += 1
            pq = []
        else:
            comp = False
            break
    if sx<start_month or ( sx==start_month and sy<= start_day):
        heappush(pq, (-ex, -ey))
        continue

if comp and (start_month<11 or (start_month == 11 and start_day<=30)):
    if not pq or (-pq[0][0] < 11 or (-pq[0][0] == 11 and -pq[0][1]<=30)):
        comp = False
    else:
        ans += 1
if comp:
    print(ans)
else:
    print(0)