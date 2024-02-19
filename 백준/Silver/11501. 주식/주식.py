
t= int(input())

for _ in range(t):
    n= int(input())
    chart = list(map(int,input().split()))

# 1 3 5 5 4 2 10 2 1 3 1
    chart.reverse()
    margin = 0
    max_target = chart[0]
    for i in range(1, n):
        if max_target < chart[i]:
            max_target = chart[i]
        else:
            margin+=max_target- chart[i]
    print(margin)