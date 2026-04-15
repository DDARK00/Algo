import math
a,b,x,y,p,q=map(int,open(0).read().split())
g=math.gcd(p,q)
p//=g;q//=g
while p*(x-a)+q*(y-b)<0:x+=p;y+=q
print(x,y)