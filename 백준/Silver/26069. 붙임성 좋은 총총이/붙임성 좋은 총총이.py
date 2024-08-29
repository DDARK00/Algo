n = int(input())

obj = {}
for i in range(n):
    ai, bi = input().split()

    if ai == "ChongChong":
        obj[bi] = 1
    if bi == "ChongChong":
        obj[ai] = 1

    if obj.get(ai):
        obj[bi] = 1
    if obj.get(bi):
        obj[ai] = 1

cnt = 0
for v in obj.values():
    if v:
        cnt += 1
print(cnt)
