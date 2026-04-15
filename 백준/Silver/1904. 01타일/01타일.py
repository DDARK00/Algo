import sys
input=sys.stdin.readline

MOD=15746
lst=[1,2,3]
for _ in range(int(input())-1):
    nxt=(lst[1]+lst[2])%MOD
    lst=[lst[1],lst[2],nxt]

print(lst[0])