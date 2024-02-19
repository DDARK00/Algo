import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())

    mbti_list = input().split()
    # 16 가지 유형 생일 문제
    # 32명이면 32개
    # 33명이면 16 16 1
    if n < 33:

        min_val = 24
        for i in range(n):
            for j in range(i + 1, n):
                for l in range(j + 1, n):
                    val = 0
                    for k in range(4):
                        if mbti_list[i][k] != mbti_list[j][k]:
                            val += 1
                        if mbti_list[i][k] != mbti_list[l][k]:
                            val += 1
                        if mbti_list[j][k] != mbti_list[l][k]:
                            val += 1
                        if val > min_val:
                            break
                    min_val = min(val, min_val)

                    if val == 0:
                        break
        print(min_val)
    else:
        print(0)
