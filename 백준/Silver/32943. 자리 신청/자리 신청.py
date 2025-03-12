n,c,k=map(int, input().split())

seat=[0]*(c+1)
stu=[0]*(n+1)
for _, s, n in sorted([tuple(map(int,input().split())) for _ in range(k)]):
    if seat[s] == 0:
        seat[stu[n]]=0
        seat[s]=1
        stu[n]=s

for idx, num in enumerate(stu):
    if num:
        print(idx, num)