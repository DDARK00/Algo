t = int(input())

lst = [[0,0]for _ in range(t)]

for i in range(t):
    a, b =input().split()
    lst[i][0] = int(a)
    lst[i][1] = b

lst.sort(key= lambda x : (x[0]))

for e in lst:
    print(e[0],e[1])
   
# 파이썬 정렬은 원본 순서 보장됨... 