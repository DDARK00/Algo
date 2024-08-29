import sys
input = sys.stdin.readline

n = int(input().strip())
obj={}
# 문자열의 길이는 50을 넘지 않는다.

for i in range(51):
    obj[i] = []

se = set()

for i in range(n):
    se.add(input().strip())
# set 해서 카운팅

for i in se :
    obj[len(i)].append(i)

for i in range(51):
    obj[i].sort(reverse=1)
    while obj[i]:
        print(obj[i].pop())