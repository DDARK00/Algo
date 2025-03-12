import sys
input=sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()

print(f'{(round(sum(lst)/n))}')
print(lst[n//2])

lst.sort()
g = [[0,i] for i in range(8001)]
for num in lst:
    g[num+4000][0] +=1
g = list(map(lambda x: [x[0], x[1]-4000] ,filter(lambda x: x[0]>0, g)))
g.sort(key = lambda x: (-x[0],x[1]))

if n>1 and g[0][0] == g[1][0]:
    print(g[1][1])
else:
    print(g[0][1])
print(lst[-1]-lst[0])