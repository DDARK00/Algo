import sys
import heapq

input = sys.stdin.readline

n = int(input())
# 컴퓨터의 수 (노드 수
m = int(input())
# 연결할 수 있는 선의 수 (간선 수


graph = [[0] * n for _ in range(n)]

for _ in range(m):
    s, e, w = map(int, input().split())
    # 스타트 엔드 웨이트
    graph[s - 1][e - 1] = w
    graph[e - 1][s - 1] = w

# n*n 가중치 배열

visited = [0] * n
hq = []
heapq.heappush(hq, (0, 0))
# 0번에서 시작
weight = 0
while hq:
    w, v = heapq.heappop(hq)
    # print(hq)
    if not visited[v]:
        # print(w, v)
        visited[v] = 1
        weight += w

        for i in range(n):
            if graph[v][i] != 0 and not visited[i]:
                heapq.heappush(hq, (graph[v][i], i))
print(weight)
