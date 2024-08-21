import sys
input = sys.stdin.readline

n = int(input())

lst = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
money = 0
for idx in range(n):
    target = lst[idx][0]
    temp = 0
    for i in range(n):
        fee = lst[i][1]
        want = lst[i][0]
        if want>=target:
        
            temp += 0 if target - fee < 0 else target - fee

    if money<temp:
        money = temp
        ans = target
    elif money == temp and target<ans:
        ans = target
print(ans)