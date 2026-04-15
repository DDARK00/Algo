while True:
    n=int(input())
    if n==0:break
    print(sorted([(x:=input(),x.lower())for _ in range(n)],key=lambda x:x[1])[0][0])