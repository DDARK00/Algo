T = int(input())

for t in range(T):
    n = int(input())
    
    max_sulgorae = 0
    max_name = ""
    for i in range(n):
        ar = input().split()
        target = int(ar[1])
        if max_sulgorae < target :
            max_sulgorae = target
            max_name = ar[0]
    print(max_name)