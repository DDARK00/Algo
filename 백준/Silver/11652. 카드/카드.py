# print(2**62)
# -4611686018427387904 ~ +4611686018427387904
# 4백6십1일 경
import sys

input = sys.stdin.readline

n = int(input())

obj = {}

ic = 0
while ic < n:
    target = int(input())
    if obj.get(target):
        obj[target] += 1
    else:
        obj[target] = 1
    ic += 1

items = list(obj.items())
items.sort(key=lambda x: (-x[1], x[0]))
# 10만개 On 가능? 가능이지~
print(items[0][0])
