cost = 105.6

for _ in range(int(input())):
    a, m = map(int, input().split())
    print(int(a*m*cost/1000/60))