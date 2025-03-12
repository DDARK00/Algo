dart = list(map(int, input().split()))

sums = 0

for i in range(20):
    if dart[i] == 20:
        a = (dart[i-1] + dart[i] + dart[(i+1)%20])/3
    sums += dart[i]

b = sums/20
if a==b:
    print("Tie")
elif a>b:
    print("Alice")
else:
    print("Bob")