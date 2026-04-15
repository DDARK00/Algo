import sys
input=sys.stdin.readline
s=input().rstrip()

d={"P":[0]*14,"H":[0]*14,"K":[0]*14,"T":[0]*14}

for i in range(0,len(s),3):
    head=s[i]
    no=int(s[i+1]+s[i+2])
    if d[head][no]:
        print("GRESKA")
        exit()
    d[head][no]=1

print(13-sum(d["P"]),13-sum(d["K"]),13-sum(d["H"]),13-sum(d["T"]))