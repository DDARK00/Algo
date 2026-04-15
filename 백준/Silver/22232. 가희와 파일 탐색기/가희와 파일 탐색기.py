import sys
input=sys.stdin.readline
n, m = map(int, input().split())

datas =[input().rstrip().split(".") for _ in range(n)]
ext = {input().rstrip():0 for _ in range(m)}

datas.sort(key=lambda x: (x[0],ext.get(x[1],2),x[1]))

for data in datas:
    print(".".join(data))