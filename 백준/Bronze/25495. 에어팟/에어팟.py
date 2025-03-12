input()
now = 0
idx = -1
spent = 2
for num in list(map(int, input().split())):
    if num == idx:
        spent*=2

    else:
        idx = num
        spent=2
    now+=spent
    if now>=100:
        now = 0
        idx = -1
        spent = 2
print(now)