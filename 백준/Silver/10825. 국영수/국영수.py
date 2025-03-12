import sys
input=sys.stdin.readline
 
n=int(input())
lst = []
 
for i in range(n):
    a,b,c,d=input().split()
    lst.append((-int(b),int(c),-int(d),a))
 
for l in sorted(lst):
    print(l[3])