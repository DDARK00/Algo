import sys
input = sys.stdin.readline

n, m = map(int,input().split())

erda = list(map(int,input().split())) # 100
ori = list(map(int,input().split())) # 360

erda.sort()
ori.sort()

can_erda = 0
erda_cnt = 0

for e in erda:
    if e>=can_erda:

        erda_cnt+=1
        can_erda = e+100

can_ori = 0
ori_cnt = 0

for o in ori:
    if o>=can_ori:

        ori_cnt+=1
        can_ori = o+360

print(erda_cnt, ori_cnt)