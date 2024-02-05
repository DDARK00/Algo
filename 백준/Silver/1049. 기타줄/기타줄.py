n, m = map(int, input().split())
# N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.

# 둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다.
# 가격은 0보다 크거나 같고,
# 1,000보다 작거나 같은 정수이다.

# 패키지 => 6개
# 패키지+낱개 vs 풀 패키지 vs 풀 낱개
# 그리디네?

pack = []
unit = []

for _ in range(m):
    p, u = map(int, input().split())
    pack.append(p)
    unit.append(u)
    # 필요한 수 n
pack.sort()
unit.sort()

p_n = n // 6
added = 0 if n % 6 == 0 else 1
etc = n % 6

min1us = min(pack[0] * (p_n + added), pack[0] * p_n + etc * unit[0])
# 패키지만 산 거vs 패키지+낱개

min1us = min(min1us, unit[0] * n)
# 위의 것 vs 낱개 둘둘

print(min1us)
