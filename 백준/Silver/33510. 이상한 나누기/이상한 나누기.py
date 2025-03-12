import sys
input=sys.stdin.readline
x=int(input())
s=input().rstrip()

if s == "1":
    print(0)
    exit()

ans = 0
flag = False
for i in range(x-1):
    if flag and s[-1-i]=="0":
        ans+=1;
    elif not flag and s[-1-i]=="1":
        flag=True
        ans+=1
print(ans)

"""
s=int(s,2)
print(s)
ans = 0;
while s>1:
    if s%2:
        ans+=1
        s+=1
    s >>= 1
print(ans)
# 1000 0
# 1010 2
# 1011 2
# +1이 0을 먹음
"""