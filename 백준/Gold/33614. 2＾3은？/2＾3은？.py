import sys
input=sys.stdin.readline
 
for _ in range(int(input())):
    p,q,r=map(int,input().split())
    print(p-1+min(q,r))
    """
    for i in range(1,p+1):
        for j in range(1,q+1):
            for k in range(1,1+r):
                a=i^j^k
                b=i**(j**k)
                if a==b:
                    print(a,b,"ans : ", a==b,i,j,k)
    """