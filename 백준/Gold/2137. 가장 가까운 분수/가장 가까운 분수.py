import sys
x, y = map(int,sys.stdin.readline().split())

ans = 1
# x/y * y/x = 1
t=x/y
a, b = 0, 0
for i in range(32767, 1, -1): #분모가 i라면
    #분자는 x/y * i
    j=i*x//y
    for k in [j+1, j]:
        if abs(t-k/i)<=ans:
            # 분자 분모가 x y가 아니면
            # j/i == x/y
            if k*y != x*i:
                ans = abs(t-k/i)
                a, b = i, k
print(b, a)