import sys

input = sys.stdin.readline

n, m = map(int,input().split())

#n+1개 m쿼리

par = [i for i in range(n+1)]

def chkpar(idx):

    if idx == par[idx]:

        return idx

    else:

        par[idx] = chkpar(par[idx])

        return par[idx]

    

for _ in range(m):

    a, b, c = map(int,input().split())

    if a:

        if chkpar(b)==chkpar(c):

            print("yes")

        else:

            print("no")

    else:

        #합집합

        b_p = chkpar(b)

        c_p = chkpar(c)

        par[c_p] = b_p

        # 오답1. 부모의 부모를 바꿔야 된다

        

# 합집합때 트리 높이는 어떻게 맞춤...?

# 괜히 값 튜플로 넣었다가 조회등등등에 더 걸리려나