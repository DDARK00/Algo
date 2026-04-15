import sys
input=sys.stdin.readline

k=int(input())

# 10 11 100 101 110 111   +1
# 4 7 44 47 74 77 444
# 1 3  7 15 31 63
# 2 4  8 16 32 64

# 1 2 3 4 5 6
# k=1 1 1
# k=8 4  1000
# k=12 4  1100
# k=16 5 10000

# 1 4 0
# 2 7 1

for c in bin(k+1)[3:]:
    if c=="0":
        print(4,end="")
    else:
        print(7,end="")