import sys
from collections import defaultdict
input=sys.stdin.readline

n,m,q=map(int,input().split())
group=defaultdict(list)
stock=defaultdict(int)

for _ in range(n):
    g,h,p=input().split() # 그룹 이름 가격
    g,p=int(g),int(p)
    group[g].append(h)
    stock[h]=p

my_stock=defaultdict(int)
def c1(A,B):
    B=int(B)
    global m
    if m>=stock[A]*B:
        m-=stock[A]*B
        my_stock[A]+=B

def c2(A,B):
    B=int(B)
    global m
    if my_stock[A]>=0:
        m+=min(my_stock[A],B)*stock[A]
        my_stock[A]-=min(my_stock[A],B)

def c3(A,B):
    B=int(B)
    global m
    stock[A]+=B

def c4(A,B):
    A=int(A)
    B=int(B)
    global m
    for k in group[A]:
        stock[k]+=B

def c5(A,B):
    A,B=int(A),int(B)
    global m
    for k in group[A]:
        stock[k]=stock[k]*(100+B)//1000*10

def c6(A,B):
    print(m)

def c7(A,B):
    rst=m
    for k, v in my_stock.items():
        rst+=stock[k]*v
    print(rst)

for _ in range(q):
    cmd,A,B,*_=(input()+" . . ").split()
    [_,c1,c2,c3,c4,c5,c6,c7][int(cmd)](A,B)

