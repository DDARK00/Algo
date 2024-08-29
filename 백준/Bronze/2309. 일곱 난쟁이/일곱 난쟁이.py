
talls = [0] * 9

diff = -100
for i in range(9):
    tall = int(input())
    talls[i] = tall
    diff += tall

talls.sort()
# 투 포인터
lp = 0
rp = 8
while lp<rp:
    sum = talls[lp] + talls[rp]
    if sum<diff:
        lp+=1
    if sum>diff:
        rp-=1
    if sum == diff:
        break

for i in range(9):
    if i in[lp, rp]:
        continue
    else:
        print(talls[i])