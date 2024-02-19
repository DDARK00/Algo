import sys

input = sys.stdin.readline

n = int(input())

# 1~4 0

# 5~9 1   5 1

# 10~14 2 5 2

# 15~19 3 5 3

# 20~24 4 5 2 2

# 25~29 6 5 5

# 30~34 7 5 2 2 2

# 35~39 8 5 7

# 40~44 9 5 2 2 2

# 45~49 10 5 3 3

# 50 12 5 5 2

# 100 24 5 5 4 20 4

# 1000 249 

# 200 40 8 1

# 아니 개어려워

answer=0

while n>4:

    answer+= n//5

    n //=5

print(answer)