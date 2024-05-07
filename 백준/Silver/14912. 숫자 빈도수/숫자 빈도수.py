n,k = map(int,input().split())

lst = [0]*10

for i in range(1,n+1):

    for x in str(i):

        lst[int(x)]+=1

print(lst[k])