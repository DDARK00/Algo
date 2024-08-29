import sys

input = sys.stdin.readline

n,m =map(int,input().split())

# 최대 n개 m명

lst = [int(input()) for _ in range(m)]

lst.sort()

length = min(n,m)

m_v = 0

val = 0

for i in range(length):

    now = lst[-i-1]

    if now*(i+1)>m_v:

        val = now

        m_v = now*(i+1)

print(val, m_v)