n = int(input())
# n개의 숫자

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# a를 재배치한다

sorted_a = sorted(a_list, reverse=True)
sorted_b = sorted(b_list)
# 시간 제한 2초~~

# 1 1 0 1 6   ->18
# 2 7 8 3 1

# 6 1 1 1 0
# 1 2 3 7 8
minsum = 0
for b in b_list:
    # b의 정렬된 위치 = a의 정렬된 위치
    idx = sorted_b.index(b)
    minsum += b*sorted_a[idx]

    #작업 하고 없애주기
    sorted_b.pop(idx)
    sorted_a.pop(idx)
print(minsum)
