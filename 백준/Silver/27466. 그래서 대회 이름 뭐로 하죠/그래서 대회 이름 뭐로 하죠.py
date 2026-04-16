import sys
input=sys.stdin.readline

n, m=map(int,input().split())
s=input().rstrip()

answer=[""]*(m)
step=0
for i in range(n-1,-1,-1):
    if n-i+m-step <0 or step==m:
        break

    if step==0:
        if s[i] not in "AEIOU":
            answer[m-step-1]=s[i]
            step+=1
    elif step==1:
        if s[i]=="A":
            answer[m-step-1]="A"
            step+=1
    elif step==2:
        if s[i]=="A":
            answer[m-step-1]="A"
            step+=1
    else: # 3
        answer[m-step-1]=s[i]
        step+=1

if step==m:
    print("YES")
    print(*answer,sep="")
else:
    print("NO")