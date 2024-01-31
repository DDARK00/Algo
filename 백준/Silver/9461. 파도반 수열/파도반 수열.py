T = int(input())

dpt = [0] * 101

dpt[0] = 0
dpt[1] = 1
dpt[2] = 1
dpt[3] = 1

for i in range(4, 101):
    dpt[i] = dpt[i - 2] + dpt[i - 3]
# print(dpt)

for t in range(T):
    n = int(input())
    print(dpt[n])
