import sys
input=sys.stdin.readline

l=[int(input()) for _ in range(int(input()))]
l.sort()

p=[]
for i in range(3):
    for j in range(i+1,min(len(l),4)):
        p.append(int(str(l[i])+str(l[j])))
        p.append(int(str(l[j])+str(l[i])))
print(sorted(p)[2])
# 1 2 3 4 12 13 14