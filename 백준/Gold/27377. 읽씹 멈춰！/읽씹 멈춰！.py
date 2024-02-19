# 17 1 5  14

# 17 8 + 5 + 1 14

# 17 6 12 11

# 5 3

# 복붙을 두 번 하면 1 2 4 야? 123이야?

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    #테케 수

    n = int(input())

    # 보낼 말 길이

    s, t = map(int,input().split())

    #하나, 복붙 시간

    # 치는 시간>복붙이면 +복붙

    # 아니면 그냥 치기

    # 복붙->2배 만들기 - 그리디

    # 이렇게 쉬울 리가 없는데...?

    # 쉬울 리가 없는데 그것도 제대로 못했다

    rst = 0

    while n>0:

        # print(n, rst)

        if n%2:

            #홀수면

            if (n-1) //2*s >t:

                n = (n-1)//2

                rst+=t + s

            else:

                rst+= s*n

                break

                

        else:

            #짝수면

            if n//2 *s> t:

                n//=2

                rst+=t

            else:

                rst+= s*n

                break

    print(rst)

# 17 3 5

# 16 3  8 5  4 5  2 5  6