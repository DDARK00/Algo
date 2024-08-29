import sys
input = sys.stdin.readline

n, score, p = map(int, input().split())
if n == 0:
    print(1)
    exit()
rank = list(map(int, input().split()))

rank.sort(key=lambda x:-x)

if len(rank)==p and rank[-1]>= score:
    print(-1)
    exit()
for idx, num in enumerate(rank):
    if num<=score:
        print(idx+1)
        exit()

print(n+1)