import sys
input=sys.stdin.readline

s=input().rstrip()
ans=s[:2]+s[2:][::-1]

for i in range(1,len(s)):
    for j in range(i+1,len(s)):
        a,b,c=s[:i][::-1],s[i:j][::-1],s[j:][::-1]
        ans=sorted([ans,a+b+c])[0]
print(ans)