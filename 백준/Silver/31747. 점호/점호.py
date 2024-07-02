import sys

from collections import deque

input = sys.stdin.readline

# N명 k번

n, k = map(int,input().split())

lst = deque(list(map(int,input().split())))

ks=[0,0,0]

cnt = 0

turn = 0

while lst or cnt>0:

    turn += 1

    while cnt<k and lst:

        target = lst.popleft()

        cnt+=1

        ks[target]+=1

    if ks[1]>0:

        ks[1]-=1

        cnt-=1

    if ks[2]>0:

        ks[2]-=1

        cnt-=1

print(turn)