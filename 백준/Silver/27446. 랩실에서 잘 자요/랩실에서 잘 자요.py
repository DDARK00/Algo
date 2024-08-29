import sys

input = sys.stdin.readline

n,m = map(int,input().split())

# n까지 m개있음

chk = [1]*(n+1) # nm<=100

for num in list(map(int,input().split())):

    chk[num] = 0

want = []

for i in range(1,n+1):

    if chk[i]:

        want.append(i)

# print(want)

# 없는거 점렬된 상태

# 5+2k

# 2 101 vs 11 11 14

# 2 1001 vs 11 13 14

# 2 10001 vs 11 15 14 false

# 12345  1+4

start = -99

cost = 0

# print(want)

for i in range(len(want)):

    # print(cost)

    now = want[i]

    if start+4> now:

        cost+=2*(now-start)

        

    else:

        cost+=7

    start = now

print(cost)

# 약간 스위핑 느낌도 나네 다르지만...