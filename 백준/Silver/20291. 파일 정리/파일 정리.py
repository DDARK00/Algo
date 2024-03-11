import sys

input = sys.stdin.readline

n = int(input())
# 문자 수

obj = {}

for _ in range(n):
    a = input()
    tail = a.strip().split(".")[1]
    # 점은 정확히 한 번 등장하며
    if obj.get(tail):
        obj[tail] += 1
    else:
        obj[tail] = 1

for key in sorted(list(obj.keys())):
    print(key, obj[key])
# 확장자 이름의 사전순으로 출력한다.
