import sys

input = sys.stdin.readline

n = int(input())

def dfs(d, k):

    global vs

    if vs == 0:

        return

    if d == n//2:

        

        st = []

        for i in range(n):

            if used[i]:

                st.append(i)

                

        s_power = 0

        l_power = 0

        

        for i in range(n//2):

            for s in st:

                s_power+=lst[st[i]][s]

            for l in other:

                l_power+=lst[other[i]][l]

        vs = min(vs,abs(s_power-l_power))

        return

        

    for i in range(k,n):

        if used[i] :

            used[i]=0

            other.append(i)

            dfs(d+1,i+1)

            other.pop()

            used[i]=1

    

vs = 999999

used = [1]*n

lst = [list(map(int,input().split())) for _ in range(n)]

other = []

dfs(0,0)

print(vs)