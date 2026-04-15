import sys
input=sys.stdin.readline

def dfs(depth,n):
    global answer
    if depth==n-1:
        if int("".join(select))>=target:
            return
        answer=max(int("".join(select)),answer)
        return

    for i in range(n):
        if use[i]:
            continue
        use[i]=1
        select.append(Alice[i])
        dfs(depth+1,n)
        select.pop()
        use[i]=0

# 답은 같은 자릿수 or 자릿수-1의 최댓값
def solve(n, target):
    global select, use, Alice, answer
    Alice=list(input().rstrip())
    Alice.sort()
    Alice_min=int("".join(Alice))
    if Alice_min>=target:
        print("".join(Alice[n:0:-1]))
        return

    answer=0
    select=[]
    use=[0]*9
    for i in range(n):
        use[i]=1
        select.append(Alice[i])
        dfs(0,n)
        select.pop()
        use[i]=0
    print(answer)

for _ in range(int(input())):
    n=int(input())
    Bob=input().rstrip()
    target=min(int(Bob),int(Bob[::-1]))

    solve(n, target)
