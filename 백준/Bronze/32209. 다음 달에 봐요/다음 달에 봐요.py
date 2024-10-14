import sys
input = sys.stdin.readline

n = int(input())

q = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a == 1 :
        q+=b
    else:
        q-=b
    if q<0 :
        print("Adios")
        exit()
print("See you next month")