import sys
input = sys.stdin.readline
n,m = map(int,input().split())
half = m/2
ans = 0
for _ in range(n):
    cnt = 0
    for c in list(input().strip()):

        if c == "O":
            cnt+=1
    if cnt>half:
        ans+=1
print(ans)