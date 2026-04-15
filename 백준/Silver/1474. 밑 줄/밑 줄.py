import sys
input=sys.stdin.readline
n, m = map(int,input().split())
lst = [input().rstrip() for _ in range(n)]

# m글자 만들기
# 대문자 뒤의 문자부터 채우기
k=m-sum(map(len,lst))-n+1
l=k//(n-1)+1
k%=(n-1)
big=[]
small=[]

target={0:0}
for i in range(1,n):
    target[i]=l
    if lst[i][0].isupper():
        big.append(i)
    else:
        small.append(i)

while k>0:
    i=0
    while k>0 and i<len(small):
        target[small[i]]+=1
        i+=1
        k-=1
    i=len(big)-1
    while k>0 and i>=0:
        target[big[i]]+=1
        i-=1
        k-=1

for i in range(n):
    print(target[i]*"_",lst[i],sep="",end="")