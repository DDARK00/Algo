m=0
idx=0
for i in range(1,6):
    v=sum(map(int,input().split()))
    if m<v:
        m=v
        idx=i
print(idx, m)