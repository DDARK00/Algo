n=int(input())

lst=[tuple(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x:(-x[2]))
chk=[0]*101
index=0
k=0
while k<3:
    if chk[lst[index][0]]==2:
        index+=1
        continue
    chk[lst[index][0]]+=1
    print(lst[index][0],lst[index][1])
    index+=1
    k+=1