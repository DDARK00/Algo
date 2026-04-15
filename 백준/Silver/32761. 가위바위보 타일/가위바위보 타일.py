import sys
input=sys.stdin.readline

n=int(input())
s=input().rstrip()
# r s p 0 1 2
answer=n
chk={"R":0,"S":1,"P":2}
def solve(k):
    global answer

    lst=[]
    target=(k-1+3)%3
    for c in s:
        if chk[c]==k:
            lst.append(chk[c])
            k=(k+1)%3

    for i in range(len(lst)-1,-1,-1):
        if lst[i]==target:
            break
        lst.pop()
    answer=min(answer,n-len(lst))
solve(0)
solve(1)
solve(2)

print(answer)