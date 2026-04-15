import sys
s=sys.stdin.readline().rstrip()

ans=[]
for i in range(len(s)-2):
    for j in range(i+1,len(s)-1):
        for k in range(j+1,len(s)):
            one,two,three=map(reversed,(s[:j],s[j:k],s[k:]))
            ans.append("".join([*one,*two,*three]))
ans.sort()
print(ans[0])