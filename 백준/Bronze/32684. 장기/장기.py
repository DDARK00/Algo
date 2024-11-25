p=[13, 7, 5, 3, 3, 2]
a = sum([x*y for x,y in zip(map(int, input().split()),p)])
b = sum([x*y for x,y in zip(map(int, input().split()),p)])
print("cocjr0208"if a>b+1.5 else "ekwoo")