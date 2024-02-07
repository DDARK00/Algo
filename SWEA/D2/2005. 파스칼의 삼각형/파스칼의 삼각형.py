T = int(input())

# dp밖에 없나..
# 그 막 조합의 수 그런거로도 배웠던거 같은데 기억이 안 남;;
# 파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

for t in range(1, T + 1):
    n = int(input())
    print(f'#{t}')
    if n >= 1:
        print("1")

    if n >= 2:
        print("1 1")
    # 2까지만 초기 설정

    if n >= 3:
        memo = [1, 1]
        for i in range(3, n + 1):
            temp = [1]
            for j in range(2, i):
                temp.append(memo[j - 2] + memo[j - 1])
            temp.append(1)
            memo = temp
            print(" ".join(list(map(str, temp))))
        # 스트링 변환
