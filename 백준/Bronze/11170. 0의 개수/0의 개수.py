import sys;input=sys.stdin.readline
ar = [0]*1000002
ar[1] = 1
for i in range(2, 1000002):
    cnt = 0
    for c in str(i-1):
        if c=="0":
            cnt+=1
    ar[i] = ar[i-1]+cnt

for _ in range(int(input())):
    a, b=map(int,input().split())
    print(ar[b+1]-ar[a])