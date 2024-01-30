T = int(input())

lst = []
    
for t in range(1,T+1):
    dep_human = list(map(int, input().split()))
    sums = 0
    for i in range(dep_human[0]):
        sums+= dep_human[i+1]
    lst.append(sums)
# print(lst)
lst.sort()

sums = 0
length = len(lst)
for i in lst:
    sums += i* length
    length-=1
print(sums)

