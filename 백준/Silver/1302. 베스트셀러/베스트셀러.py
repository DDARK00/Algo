n = int(input())

obj = {}

for i in range(n):
    target = input()
    if obj.get(target):
        obj[target] += 1
    else:
        obj[target] = 1

lst = list(obj.items())
lst.sort(key=lambda x: (-x[1], x[0]))
print(lst[0][0])
