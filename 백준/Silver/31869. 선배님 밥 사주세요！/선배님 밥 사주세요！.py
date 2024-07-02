import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    s, w, d, p = input().split()
    plan = int(w)*7+int(d)
    lst.append((s,plan,int(p)))
lst.sort(key = lambda x:x[1])

senpai = {}
for _ in range(n):
    name, money = input().split()
    senpai[name] = int(money)

max_day = 0
today = None
ren_day = 0
for name, day, money in lst:
    if today == day:
        continue
    if senpai[name] >= money:
        if today != None and today +1 == day :
            ren_day +=1
        else:
            ren_day = 1
        max_day = max(max_day, ren_day)
        today = day
print(max_day)
        