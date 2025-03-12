import sys
input=sys.stdin.readline
 
n=int(input())
origin=list(map(int,input().split()))
chk = list(map(int,input().split()))
 
def straight():
    st = origin.index(chk[0])
 
    isok = True
    for i in range(n):
        idx = (st+i)%n
        if chk[i] != origin[idx]:
            isok = False
            break
    return isok
 
def reverse():
    chk.reverse()
    return straight()
 
if straight() or reverse():
    print("good puzzle")
else:
    print("bad puzzle")