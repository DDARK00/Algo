import sys
input=sys.stdin.readline

n,q=map(int,input().split())
s=list(input().rstrip())

for _ in range(q):
    k,l,r=map(int,input().split())
    if k==1:
        cnt=1
        bf=s[l-1]
        rst=[]
        for i in range(l,r):
            if bf != s[i]:
                bf=s[i]
                rst.append(cnt)
                cnt=1
            else:
                cnt+=1
        rst.append(cnt)
        print(len(rst))
    elif k==2:
        for i in range(l-1,r):
            s[i]=chr((ord(s[i])-65+1)%26+65)