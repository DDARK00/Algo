import sys
input=sys.stdin.readline

def chk(s):
    rst=0
    for c in s:
        if int(c)%2:rst+=1
    return rst

def solve(k):
    cnt=chk(k)
    mn,mx=1e9,0
    if len(k)==1:
        mn,mx=0,0
    elif len(k)==2:
        nxt=int(k[0])+int(k[1])
        t_mn,t_mx=solve(str(nxt))
        mn,mx=t_mn,t_mx
    else:
        for i in range(1,len(k)-1):
            #t_mx,t_mn=0,1e9
            for j in range(i+1,len(k)):
                s1=k[:i]
                s2=k[i:j]
                s3=k[j:]
                tmp=solve(str(sum(map(int,(s1,s2,s3)))))
                mn=min(mn,tmp[0])
                mx=max(mx,tmp[1])
            #mn=min(mn,t_mn)
            #mx=max(mx,t_mx)

    return (mn+cnt,mx+cnt)

s=input().rstrip()
mn,mx=1e9, -1
# 1e9 1000000000 n^2 100
if len(s)>2:
    for i in range(1,len(s)-1):
        cnt=chk(s)
        for j in range(i+1,len(s)):
            s1=s[:i]
            s2=s[i:j]
            s3=s[j:]
            t_mn,t_mx=solve(str(sum(map(int,(s1,s2,s3)))))
            mn=min(mn,cnt+t_mn)
            mx=max(mx,cnt+t_mx)

else:
    mn,mx=solve(s)

print(mn,mx)