import sys

input = sys.stdin.readline

s1 = input()

s2 = input()

# s2의 문자가 s1에 있는가

i = 0

for i in range(10):

    s1 = s1.replace(str(i), "")

if s2 in s1:

    print(1)

else:

    print(0)