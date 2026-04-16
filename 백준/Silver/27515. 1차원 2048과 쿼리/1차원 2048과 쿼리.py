import sys
input=sys.stdin.readline

n=int(input())
total=0
for _ in range(n):
    q=int(input())
    total+=q
    if total==0:
        print(0)
    else:
        print(1<<(total.bit_length()-1))