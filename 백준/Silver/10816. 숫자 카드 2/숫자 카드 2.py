import sys

input = sys.stdin.readline

tcnt = int(input())

txt = input().split()

obj = {}

for t in txt:

    if obj.get(t):

        obj[t]+=1

    else:

        obj[t]=1

qcnt = int(input())

q = input().split()

for qq in q :

    if obj.get(qq):

        print(obj[qq], end=" ")

    else:

        print(0, end=" ")