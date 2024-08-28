import sys
input = sys.stdin.readline

n, h = map(int, input().split())

# cards hp

lst = list(map(int, input().split()))
lst.sort(reverse=True)

cnt = 0
while lst and h>0:
    h-=lst.pop()
    cnt+=1

if h<=0:
    print(cnt)
else:
    print(-1)