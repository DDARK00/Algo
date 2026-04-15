import sys
input=sys.stdin.readline
while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    p=b-a
    q=c-b
    if p==q:
        print("AP",c+p)
    else:
        print("GP",c*(b//a))