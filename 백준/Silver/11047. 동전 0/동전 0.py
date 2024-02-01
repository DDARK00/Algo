n, k = map(int, input().split())
# n은 지폐의 수~ k는 돈

# 잔돈 나누기랑 완전히 똑같음

don_jongryu = [0] * n
for i in range(n):
    don_jongryu[i] = int(input())

cnt = 0
don_jongryu.sort(reverse=1)

for don in don_jongryu:
    if k == 0: break
    cnt += k // don
    k = k % don

print(cnt)
