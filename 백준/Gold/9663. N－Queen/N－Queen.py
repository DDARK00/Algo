# T = int(input())


# 공략 안 보고 일단 두뇌 풀가동 #1 #2 #3
# 힌트 : 완전탐색 + 백트래킹
import sys
input = sys.stdin.readline

def dfs(qc, start):
    # -----------
    # n - start -> 채워진 queen 수
    # ar의 start
    # -----------

    global cnt

    if qc == 0:
        # 여기까지 들어왔으면 -> 가능한 경우
        cnt += 1
        # print(jar)

    else:

        for k in range(n):
            if k not in jar:
                if start - k not in card and start + k not in caru:
                    jar.append(k)
                    # j의 위치

                    caru.append(start + k)
                    card.append(start - k)
                    # 대각선
                    # 4,3 ->  3,2  3,4 5,2 5,4
                    # 합 7 차 1 1   7 7   1

                    # k가 0부터 n-1까지, 0,k 의 위치
                    dfs(qc - 1, start + 1)

                    jar.pop()
                    caru.pop()
                    card.pop()


# 기본 구조는 이게 맞을 것인데... 아닌가???
# + 유효성 검증
# 일차원배열에 좌표???로 넣을까?
# 아니 백트래킹을 어디서 해야 되는 거임??
# 대각선 ij 같은값 증가 감소


# for t in range(1, T + 1):
n = int(input())
# n*n

cnt = 0
jar = []
# j축 검증 배열
caru = []
card = []
# 대각선 검증 배열
dfs(n, 0)

print(cnt)
