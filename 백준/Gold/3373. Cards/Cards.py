import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    a, b = map(int,input().split())

    if a<b:
        a, b = b, a
    lst.append((a+b,a,b))

lst.sort(key = lambda x:(x[0],x[1],x[2]))
ans = 0

for i in range(n//2):
    ans+=lst[i][2]

for i in range(n//2,n):
    ans-=lst[i][1]

print(ans)
# 어으 3시간을 보고