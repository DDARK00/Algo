T = int(input())

paper = [[0 for _ in range(101)]for _ in range(101)]
for t in range(T):
    x, y = map(int, input().split())
    # 시작점부터 10*10
    for i in range(x+1, x+11):
        for j in range(y+1, y+11):
            paper[i][j] = 1

print(sum(sum(paper,[])))