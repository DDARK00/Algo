


# def w(a,b,c):
#     w = [[[0 for i in range(21)] for j in range (21)] for l in range (21)]
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     elif a > 20 or b > 20 or c > 20 :
#         return w[20][20][20]
#     elif a < b and b < c :
#         return w[a][b][c-1] + w[a][b-1][c-1] - w[a][b-1][c]
#     else : 
#         return w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]

# abc 중 하나라도 0이면 리턴1

# abc가 20보다 큰 게 있으면 w20 20 20

# a<b<c 면  c-1 + b-1c-1 - b-1

# a b c 는 아무리 커도 20

# 아무것도 이해를 못 했는데 메모하라는 얘기 듣고 이렇게 됐음

    
w = [[[0 for _ in range(51)] for _ in range (51)] for _ in range (51)]
w[0][0][0]= 1
for a in range(51):
    for b in range(51):
        for c in range(51):
            if a <= 0 or b <= 0 or c <= 0:
                w[a][b][c]= 1
            elif a > 20 or b > 20 or c > 20 :
                w[a][b][c]= w[20][20][20]
            elif a < b and b < c :
                w[a][b][c]= w[a][b][c-1] + w[a][b-1][c-1] - w[a][b-1][c]
            else : 
                w[a][b][c]= w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]
while True:
    n, m, k = map(int, input().split())
    if n == -1 and m == -1 and k == -1:
        break
    elif n <= 0 or m <= 0 or k <= 0:
        # w[n][m][k]= 1
        print(f'w({n}, {m}, {k}) = 1')
        continue
    
    if n > 20 or m > 20 or k > 20 :
        print(f'w({n}, {m}, {k}) = {w[20][20][20]}')
        continue
        
        

    print(f'w({n}, {m}, {k}) = {w[n][m][k]}')
    
    # print(a,b,c)
    
    # 
    