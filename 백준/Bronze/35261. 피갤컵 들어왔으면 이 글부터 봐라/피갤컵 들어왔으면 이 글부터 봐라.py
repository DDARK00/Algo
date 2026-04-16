import sys
input=sys.stdin.readline

n=int(input()) # 100
s=input()
ans=5
for i in range(n-4):
    ans=min(ans,5-(s[i]=='e')-(s[i+1]=='a')-(s[i+2]=='g')-(s[i+3]=='l')-(s[i+4]=='e'))
print(ans)