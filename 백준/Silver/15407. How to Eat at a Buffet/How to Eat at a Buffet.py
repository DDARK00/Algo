import sys

input = sys.stdin.readline

n = int(input()) #음식 수

a = int(input()) #용량

lst = [tuple(map(int,input().split())) for _ in range(n)]

lst.sort(key=lambda x:-x[0])

answer = 0

for val, q in lst: # 가치와 최대 양

    if a>q:

        answer += val*q

        a -= q

    else:

        answer += a*val

        break

print(answer)