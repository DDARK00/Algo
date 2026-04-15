import math
a,b,c=map(int,input().split())
print(a+math.ceil(max(0,int(input())-30)/b)*c)