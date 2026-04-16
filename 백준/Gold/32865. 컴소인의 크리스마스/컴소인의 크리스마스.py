import sys
input=sys.stdin.readline

# init
n=int(input())

s=[]
p_sum = 0
for i in range(1, n+1):
    temp = int(input())
    p_sum+=temp
    s.append([temp,i])

if p_sum != n-1:
    print(-1)
    exit()

s.sort(key=lambda x: -x[0]) # stack

# solve
solved_cnt=0
solve_waiting = [] 

now=True # True = solve / False = wa
while solved_cnt<n:
    if now: # 풀어야됨
        if solve_waiting:
            print(solve_waiting.pop(),)
        else:
            print(s.pop()[1])
        solved_cnt+=1

    else: # 틀려야됨
        while s and s[-1][0] == 0:
            solve_waiting.append(s.pop()[1])
        print(s[-1][1])
        s[-1][0]-=1
    now = not now