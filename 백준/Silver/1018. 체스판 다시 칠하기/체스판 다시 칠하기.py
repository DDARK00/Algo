a, b = map(int, input().split())

# a * b 체스판 a는 줄 수 b는 칸 수


ar = []
for i in range(a):
    ar.extend(list(input().split()))

# print(ar)
# b 칸이 12라면 0 부터 8 4  1부터 9

m_min = 64
for cr in range(a - 7):
    #     줄 이동
    for rc in range(b - 7):
        #     칸 이동
        start_black = 0
        # print(cr, rc)
        for i in range(cr, cr + 8):
            # 줄
            # sum1
            # sum2 64-sum1
            # start_white = 64-start_black
            for j in range(rc, rc + 8):
                # 1 8 1 2 3 4 5 6 7
                # 칸
                if i % 2 == 0 and j % 2 == 0:
                    if ar[i][j] == "B":
                        start_black += 1
                if i % 2 == 0 and j % 2 == 1:
                    if ar[i][j] == "W":
                        start_black += 1

                if i % 2 == 1 and j % 2 == 1:
                    if ar[i][j] == "B":
                        start_black += 1
                if i % 2 == 1 and j % 2 == 0:
                    if ar[i][j] == "W":
                        start_black +=1
        # print(start_black)
        start_white = 64 - start_black
        min_v = min(start_black, start_white)
        if m_min>min_v : m_min = min_v
        # print("-------------------")
    # i%2 0 j%2 0 B
    # i%2 0 J%2 1 W
    # i%2 1 j%2 1 B
    # i%2 1 j%2 0 W
print(m_min)