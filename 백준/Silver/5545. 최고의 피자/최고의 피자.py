import sys
input=sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
# dou top cost

c = int(input())
# dou kcal

to = [int(input()) for _ in range(n)]
# top kcal
to.sort(reverse=True)

kcal = c
money = a
for num in to:
    target = kcal/money
    if num/b > target:
        kcal += num
        money += b
    else:
        break
print(kcal//money)