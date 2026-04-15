import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
l_o=0
l_e=0
ans_o=0
ans_e=0
for i in range(n):
    if lst[i]%2:
        ans_o+=i-l_o
        l_o+=1
    else:
        ans_e+=i-l_e
        l_e+=1
print(min(ans_o,ans_e))