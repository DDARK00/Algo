import sys

tc = int(input())

for _ in range(tc):

    n = int(input())

    city = set()

    for _ in range(n):

        city.add(input().rstrip())

    print(len(city))