import sys
input=sys.stdin.readline
ans=[""]*781
color=["Violet","Indigo","Blue","Green","Yellow","Orange","Red"]

chk={425:1,450:2,495:3,570:4,590:5,620:6}
l=int(input())
idx=0
for i in range(380,781):
    if chk.get(i):
        idx=chk[i]
    ans[i]=color[idx]
print(ans[l])