for _ in range(int(input())):
    lst=list(map(int,input().split()))
    n=lst[0]
    lst=lst[1:]

    if n%2:
        print("YES")
    else:
        odd=sum(map(lambda x:1 if x[0]%2 and x[1] else 0,enumerate(lst)))
        even=sum(lst)-odd
        if abs(odd-even)>1:
            print("NO")
        else:
            print("YES")