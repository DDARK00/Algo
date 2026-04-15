while True:
    a,b,c=sorted(map(int,input().split()))
    if sum([a,b,c])==0:break
    if a+b<=c:
        print("Invalid")
    elif a==c:
        print("Equilateral")
    elif b in[a,c]:
        print("Isosceles")
    else:
        print("Scalene")