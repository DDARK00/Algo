n,h,w=map(int,input().split())
[print(["DA","NE"][h**2+w**2<int(input())**2])for _ in range(n)]