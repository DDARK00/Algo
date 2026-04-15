a,b=map(int,input().split())
n=int(input())

lst=list(map(int,input().split()))
k=lst[-1]

for i in range(1,n):
    k+=lst[-i-1]*(a**i)

answer=[]

while k>0:
    answer.append(k%b)
    k//=b
print(*reversed(answer))