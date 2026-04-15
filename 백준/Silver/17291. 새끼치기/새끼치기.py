import sys
input=sys.stdin.readline

n=int(input())
bug=[0]*(23)
bug[0]=1
bug[1]=1
for i in range(2,21):
    bug[i]=bug[i-1]*2-(1^(i%2)and(bug[i-4]+bug[i-5]))
print(bug[n])