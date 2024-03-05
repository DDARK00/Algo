T = int(input())

for t in range(1, T + 1):
    n = int(input())
    # 가진 의상 수

    # 같은 이름을 가진 의상은 존재하지 않는다.
    obj = {}
    for _ in range(n):
        a, b = input().split()
        if obj.get(b):
            obj[b] += 1
        else:
            obj[b] = 2

    vals = list(obj.values())
    ast = 1
    for i in range( len(vals)):
        ast *= vals[i]

    print(ast-1)
