import sys
input = sys.stdin.readline
n = int(input())
ans=list(map(lambda x: n if n<int(x) else int(x), input().split()))
print(sum(ans))