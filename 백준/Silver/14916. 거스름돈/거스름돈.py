n = int(input())
# 2원 5원
cnt = 0
while n % 5 != 0:
    n -= 2
    cnt += 1
cnt += (n // 5)
if n < 0:
    cnt = -1
print(cnt)
