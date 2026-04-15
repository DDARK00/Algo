dir=0 # 북 동 남 서
for _ in range(10):
    n=int(input()) # 1우 2뒤 3좌
    dir=(dir+[_,1,2,-1][n]+4)%4
print(["N","E","S","W"][dir])