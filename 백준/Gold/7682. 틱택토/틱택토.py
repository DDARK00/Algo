import sys
from collections import defaultdict
input=sys.stdin.readline

NO = "invalid"
YES = "valid"
while True:
    s = input().rstrip()
    if s == "end":
        break
    xc=s.count("X")
    oc=s.count("O")

    chk = defaultdict(int)
    for i in range(3):
        chk[s[i*3:i*3+3]]+=1
        chk[s[i]+s[3+i]+s[6+i]]+=1
    chk[s[0]+s[4]+s[8]]+=1
    chk[s[2]+s[4]+s[6]]+=1

    X = chk["XXX"]
    O = chk["OOO"]
    if X and O:
        print(NO)
        continue

    if xc==oc+1: # x win or draw
        if O or s.count(".")>0 and X==0:
            print(NO)
            continue
    elif xc==oc: # o win
        if X or s.count(".")>0 and O==0:
            print(NO)
            continue
    else:
        print(NO)
        continue
    print(YES)