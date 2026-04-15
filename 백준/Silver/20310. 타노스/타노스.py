import sys
input=sys.stdin.readline

s=input().rstrip()
cnt={'0':0,'1':0}
for c in s:
    cnt[c]+=1
cnt['0']//=2
cnt['1']//=2

for c in s:
    if c=='0':
        if cnt['0']==0:
            continue
        print(0,end="")
        cnt['0']-=1
    else:
        if cnt['1']==0:
            print(1,end="")
            continue
        cnt['1']-=1
# s=500//2 250