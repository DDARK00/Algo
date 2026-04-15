import sys
input=sys.stdin.readline

h,m,s=map(int,input().split())
k=int(input())
s=(s+k%60)
k//=60
if s>=60:
    m+=s//60
    s%=60
m=m+k%60
k//=60
if m>=60:
    h+=m//60
    m%=60
h+=k
h%=24
print(h,m,s)