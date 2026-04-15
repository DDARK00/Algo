import sys
input=sys.stdin.readline

lv=int(input())
i=500
j=300
k=100

ar=[[200, 210, 220],[210,220,225],[220,225,230],[225,230,235],[230,235,245],[235,245,250]]
gr=[[260,265,270],
[265,270,275],
[270,275,280],
[275,280,285],
[280,285,290],
[285,290,295],
[290,295,300]]

for a,b,c in ar:
    if c<=lv:
        print(k,end=" ")
    elif b<=lv:
        print(j,end=" ")
    elif a<=lv:
        print(i,end=" ")
    else:
        print(0,end=" ")
print()
for a,b,c in gr:
    if c<=lv:
        print(k,end=" ")
    elif b<=lv:
        print(j,end=" ")
    elif a<=lv:
        print(i,end=" ")
    else:
        print(0,end=" ")