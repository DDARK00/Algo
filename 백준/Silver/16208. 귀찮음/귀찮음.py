n = int(input())

n_list = list(map(int, input().split()))

bar_sum = sum(n_list)

# 그리디, 정렬해야겠쥬?

n_list.sort()

# 최소비용 -> 가장 클 때 가장 작은거 곱하기

cost = 0
# print(n_list,bar_sum)
for i in range(n - 1):
    # 마지막 막대기는 한번에 두 개 나옴 n-1
    bar_sum -= n_list[i]
    cost += bar_sum * n_list[i]

print(cost)
