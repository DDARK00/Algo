Sab = int(input()) # 고속철도
Ma, Fab, Mb = map(int,input().split())
# 공항
F = Ma+Fab+Mb
if Sab<=F or Sab<=240:
    print("high speed rail")
else:
    print("flight")