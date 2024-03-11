import sys

n = int(input())

# n*n n은 2의 배수

lst = [list(input().split()) for _ in range(n)]

def fcut (sx,sy,ex,ey):

    if ex-sx != 1 :

        cx = (ex + sx)//2

        cy = (ey + sy)//2

        # 사분면

        a = fcut(sx,sy,cx,cy)

        b = fcut(sx,cy+1,cx,ey)

        c = fcut(cx+1,sy,ex,cy)

        d = fcut(cx+1,cy+1,ex,ey)

        if a[0]==b[0]==c[0]==d[0]==1 and a[1]==b[1]==c[1]==d[1]==0:

            return 1,0

        elif a[0]==b[0]==c[0]==d[0]==0 and a[1]==b[1]==c[1]==d[1]==1:

            return 0,1

        # 하나라도 다르면 다른 거지?

        else:

            return a[0] + b[0] + c[0] + d[0], a[1] + b[1] + c[1] + d[1]

    else: 

        a = lst[sx][sy]

        b = lst[sx][ey]

        c = lst[ex][sy]

        d = lst[ex][ey]

        # print(a,b,c,d,"-->>",sx,sy,ex,ey)

        if a == b == c == d :

            # 파이썬은 이런게 되네...

            if a == "0":

                return 1,0

            else:

                return 0,1

            

        else :

            cnt = [a,b,c,d].count("0")

            return cnt, 4-cnt

            # print("?1")

# 흰색0 파란색1

ans,wer = fcut(0,0,n-1,n-1)

print(ans)

print(wer)

# 노가다하는거 맞음? ㄹㅇ루?