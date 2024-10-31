import sys;input=sys.stdin.readline

n, m  = map(int, input().split())
l = reversed(list(map(int, input().split())))
added = 0
for idx, num in enumerate(l):
    added+=num
    if added>=m:
        print(n-idx)
        exit()
print(-1)