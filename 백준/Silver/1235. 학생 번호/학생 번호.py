import sys
input=sys.stdin.readline

n=int(input())

lst = [input().rstrip() for _ in range(n)]
cnt = 0
answer = 0
while cnt != n:
    answer+=1
    cnt = len(set(map(lambda x: x[-1:-1-answer:-1], lst)))
print(answer)