a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g = a+b*2+c*3
h = d+e*2+f*3
print(int(not g == h)+int(g<h))