import sys

input = sys.stdin.readline

n = int(input())  # 전체 도시의 수
m = int(input())  # 여행 계획 도시의 수

obj = {}

lst = [list(map(int, input().split())) for _ in range(n)]
# 인접 리스트
for i in range(n):
    obj[i] = i


def check_par(city):
    # na가 target의 부모이다
    p = obj[city]
    # na의 부모가 또 있다면 찾아와야지
    if p != city:
        p = check_par(p)
    obj[city] = p
    return p
    # 경로단축


def change_par(na, target):
    par1 = check_par(na)
    par2 = check_par(target)
    if par1 != par2:
        obj[target] = par1
        obj[par2] = par1
    return


# 전처리
for i in range(n):
    for idx, val in enumerate(lst[i]):
        if val:
            change_par(i, idx)
# A와 B가 연결되었으면 B와 A도 연결되어 있다.
goto = list(map(int, input().split()))
# 일정

# print(obj)
go = True
p = check_par(goto[0] - 1)

for i in range(1, m):
    target = goto[i] - 1
    # print(check_par(target),)
    if p != check_par(target):
        go = False

if go:
    print("YES")
else:
    print("NO")
