import sys
input = sys.stdin.readline

people = set()
n = int(input())

for _ in range(n):
    a, b = input().strip().split(" ")
    if b == 'enter':
        people.add(a)
    else:
        people.remove(a)
people = list(people)
people.sort()
print(*reversed(people),sep='\n')