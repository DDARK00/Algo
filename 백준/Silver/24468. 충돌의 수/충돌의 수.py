import sys
input=sys.stdin.readline

l,n,t=map(int,input().split())
box=[[] for _ in range(l+1)] # 0, l wall 1000
dir=[0]*(n+1)

def init():
    for i in range(1,1+n):
        s,c=input().split()
        box[int(s)].append(i)
        dir[i]= 1 if c=="R" else -1

def move():
    global box
    temp=[[]for _ in range(l+1)]
    for i in range(l+1):
        for num in box[i]:
            temp[i+dir[num]].append(num)
    box=temp

def reflect(k):
    cnt=1 if len(box[k])==2 else 0
    for num in box[k]:
        dir[num]*=-1
    return cnt

def calc():
    cnt=0
    for i in range(1,l):
        if len(box[i])>1:
            cnt+=reflect(i)
    cnt+=reflect(0)
    cnt+=reflect(l)
    return cnt

answer=0
init()
for _ in range(t):
    move()
    answer +=calc()
print(answer)