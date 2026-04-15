import sys
input=sys.stdin.readline

data=[]
for _ in range(int(input())):
    x=input().rstrip()
    k=0
    for c in x:
        if c.isdigit():
            k+=int(c)
    data.append((len(x),k,x))
data.sort()
for _,_,a in data:
    print(a)