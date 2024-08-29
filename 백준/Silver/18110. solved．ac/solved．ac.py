import sys

input = sys.stdin.readline

def roundup(x:float):

    if x%1 >= 0.5 :

        return int(x)+1

    else:

        return int(x)

n = int(input())

if n == 0:

    print(0)

else:

    lst= [int(input()) for _ in range(n)]

    lst.sort()

    cut = roundup(n*0.15)

    start = cut

    end = n-cut

# print(start,end)

    print(roundup(sum(lst[start:end])/(n-cut*2)))