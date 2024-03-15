import sys

# from collections import deque

input = sys.stdin.readline

n, q = map(int, input().split())

# 수열 길이, 쿼리 수


# 세그먼트도 ok?
lst = list(map(int, input().split()))
# 수열

sub_lst = [0] * n
# 누적합
temp = 0
for i in range(n):
    temp += lst[i]
    sub_lst[i] = temp

# 1k 오른쪽으로 k만큼 이동
# 2k 왼쪽으로 k만큼 이동

# 3ab a부터 b까지의 합
index = 0
# test = deque(lst)
for _ in range(q):
    # 쿼리만큼 반복
    query = input()
    if query.startswith("1"):
        a, b = map(int, query.split())
        if b != n:

            index = (n - b + index) % n
        # for i in range(n):
        #     print(lst[(index + i) % n], end=" ")
        # print("<<-- index")
        #
            # test.rotate(b)
        # print(*list(test), "<-- test")
    elif query.startswith("2"):
        a, b = map(int, query.split())
        if b != n:

            index += b
            index %= n
        # print(lst[index], "<-- index")
        # for i in range(n):
        #     print(lst[(index + i) % n], end=" ")
        # print("<<-- index")
        #
            # test.rotate(-b)
        # print(*list(test), "<-- test")
    else:
        a, s, e = map(int, query.split())
        # s부터 e까지
        end = (index + e - 1) % n
        start = (index + s - 1) % n
        # print(start, end, s, e)
        # # print(sub_lst[end])
        # print(lst, "<<---lst")
        # for i in range(n):
        #     print(lst[(index + i) % n], end=" ")
        # print("<<-- query")
        #
        # test2 = []
        # temp2 = 0
        # for i in range(n):
        #     temp2 += test[i]
        #     test2.append(temp2)

        if start <= end:
            print(sub_lst[end] - (sub_lst[start - 1] if start != 0 else 0))

        else:

            print(temp - (sub_lst[start - 1] - sub_lst[end]))
    # 구간합
