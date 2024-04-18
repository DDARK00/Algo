import sys

input = sys.stdin.readline


def ccw(x, y, z):
    # 세 점에 대해 신발끈 공식으로 계산했을 때 -> 선분과 한 점 사이의 방향
    # 이걸 두 점(선분)과 한 점 + 다른 점(다른 선분) 에 대해서 계산하면
    # 점이 평행하면 0, 시계 반시계 양수 음수
    # 즉, 각 점에 대해서 부호가 다르게 나오면 교차 -> 곱은 음수
    val = (y[0]-x[0]) * (z[1]-x[1]) - (y[1]-x[1])*(z[0]-x[0])
    return val



x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))
dot1 = x1, y1
dot2 = x2, y2
dot3 = x3, y3
dot4 = x4, y4

c1 = ccw(dot1, dot2, dot3)
c2 = ccw(dot1, dot2, dot4)
c3 = ccw(dot3, dot4, dot1)
c4 = ccw(dot3, dot4, dot2)
# print(c1, c2, c3, c4)
if c1 * c2 < 0 and c3 * c4 < 0:
    print(1)
else:
    print(0)
