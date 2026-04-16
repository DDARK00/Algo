import sys
input=sys.stdin.readline
# 10문제중 5개의 경우의 수

ans=list(map(int,input().split()))
cnt=0
# 1 2 3 4 5
# 11 12 13 14 15
select=[0,0]
def solve(score,depth):
    global cnt
    if depth==12:
        if score>=5:
            cnt+=1
        return

    if 12-depth+score<5:
        return

    for i in range(1,6):
        if select[depth-1]==select[depth-2] and select[depth-2]==i:
            continue
        select.append(i)
        solve(score+int(ans[depth-2]==i),depth+1)
        select.pop()

solve(0,2)
print(cnt)