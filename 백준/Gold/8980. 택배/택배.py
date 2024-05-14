import sys
input = sys.stdin.readline

n, c =map(int,input().split())
# 마을, 용량

m = int(input())
# 물건 수

_w = [c]*(n+1)
# 승하차 목록(남은 무게)

lst = [tuple(map(int,input().split())) for _ in range(m)]
lst.sort(key = lambda x : (x[1],x[0]))
score = 0

for s, e, w in lst:
    can = w
    for i in range(s,e): # s에서 e로 가는동안 가능 용량
        can = min(can,_w[i])

    for i in range(s,e):
        _w[i]-=can
    # print(s,e,w,can)

    score+=can
print(score)

"""
6 80
7
1 5 50
2 3 50
2 4 50
2 6 80
3 4 50
3 6 30
4 5 50

1  2  3  4  5  6 마을 최대 80
0  0  0  0  0  0
0  50 30 50
   30 50
0  0  50 80 0  0  내림

2 3 50 정렬
2 4 50
3 4 50
1 5 50
4 5 50
2 6 80
3 6 30

스위핑 될 것 같았는데 감이 안 잡히네
"""