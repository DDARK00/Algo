import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n, m = map(int,input().split())
    # 국가의 수 비행기 수
    for _ in range(m):
        a, b = map(int , input().split())
    print(n-1)
    # 미니멈 스패닝 트리 - n-1
    # 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.
    