import sys
input=sys.stdin.readline

n=int(input())
lst=[int(input()) for _ in range(n)]

answer = n
for i in range(n):
    if lst[-1-i]==answer:
        answer-=1
print(answer)