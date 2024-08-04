import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

max_st = 0
ans = [1,1,0,0,0]
for i in range(4): # m t w t f 
    temp = []
    for p in lst:
        if p[i]:
            temp.append(p)
    if max_st>=len(temp):
        continue
    for j in range(i+1,5):
        temp2 = []
        for q in temp:
            if q[j]:
                temp2.append(q)

        if max_st<len(temp2):
            max_st = len(temp2)
            ans = [0]*5
            ans[i],ans[j]=1,1

print(max_st)
print(*ans)