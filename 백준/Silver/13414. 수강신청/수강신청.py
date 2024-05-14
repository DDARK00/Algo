import sys

input = sys.stdin.readline

k, l = map(int,input().split())

chk = {}

p_cnt = 0

lst = []

for _ in range(l):

    target = input().rstrip()

    lst.append(target)

    if chk.get(target):

        chk[target]+=1

    else:

        chk[target] = 1

        p_cnt+=1

rst_cnt = 0

for el in lst:

    if chk[el] == 1:

        print(el)

        rst_cnt+=1

    else:

        chk[el]-=1

    if rst_cnt == k:

        break