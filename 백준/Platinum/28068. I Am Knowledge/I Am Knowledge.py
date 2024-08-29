import sys
input = sys.stdin.readline

n = int(input())
# n개의 책

lst = []
for _ in range(n):
    a, b = map(int,input().split())
    # a를 소모해서 b를 얻음
    # 소모했을 때 0 미만이면 아웃
    lst.append((a,b,b-a)) # 소모량 획득량 증감
kn = 0
lst.sort(key = lambda x : (x[0], -x[2]))

wating = []
ok = 1

for lost, get, add in lst:
    if lost<= kn: # 읽을 수 있는 책
        if add>=0:
            kn+=add

        else:

            wating.append((lost,get,add))

    else:
        ok = 0
        break
wating.sort(key=lambda x:(x[1]))
# 남은건 어차피 마이너스라서 얻는게 큰 순으로 <- 이게 플래급이네 ㄹㅇ
# ㅁ?ㄹ

while ok and wating:
    lost, get, add = wating.pop()
    if kn-lost<0:
        ok = 0

    else:
        kn+=add

print(ok)