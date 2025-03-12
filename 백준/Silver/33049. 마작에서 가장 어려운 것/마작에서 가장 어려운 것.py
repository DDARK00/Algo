import sys, math
input=sys.stdin.readline
sam, sa, free = map(int, input().split())

free -= (3-sam%3)%3
free -= (4-sa%4)%4

if free <0 :
    print(-1)
    exit()

ans3 = math.ceil(sam/3)
ans4 = math.ceil(sa/4)

# x = (free-4y)/3
ans = (-1, "")
for i in range(free//4,-1,-1):
    if (free-4*i)%3 == 0:
        ans = (ans3+(free-4*i)//3, ans4+i)
        break
print(*ans)
# 코드가 점점 산으로 가냐...