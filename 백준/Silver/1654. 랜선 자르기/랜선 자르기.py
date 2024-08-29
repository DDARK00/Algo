import sys
input = sys.stdin.readline

k, n = map(int,input().split())
# 소지수, 필요수d

lst = [int(input()) for _ in range(k)]
# 만들 수 있는 최대 랜선의 길이

def calc_cnt(x):
    cnt = 0
    for l in lst:
        cnt += l//x
    return cnt
# 만들 수 있는 개수

start = 1
end = max(lst)
while start<=end:
    mid = (start+end)// 2
    find = calc_cnt(mid)
    # print(find, start, end)
    if find >= n : # 잘 만들었으면 범위를 줄이고
        start = mid + 1

    else : # 덜 만들었으면 범위를 늘리고
        end = mid - 1
print(end)
# 이분탐색보다 훨 편하다