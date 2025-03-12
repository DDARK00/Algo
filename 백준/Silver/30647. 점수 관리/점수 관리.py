import sys, re
input=sys.stdin.readline

info = []
for _ in range(int(input())):
    s = input().rstrip()
    s = re.split('":"|","|":|,"|}', s)
    info.append((s[1],int(s[3]),s[5]))
info.sort(key = lambda x:(-x[1],x[0]))

before = -1
no = 0
for idx, data in enumerate(info):
    name, score, isHidden = [*data]
    if before != score:
        before = score
        no = idx+1
    if isHidden == "0":
        print(no,name,score)