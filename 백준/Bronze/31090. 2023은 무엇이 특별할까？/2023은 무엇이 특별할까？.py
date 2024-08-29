tc = int(input())
for _ in range(tc):
    n = int(input())
    n1 = n+1
    last=n%100
    if last != 0 and n1%last == 0:
        print("Good")
    else:
        print("Bye")