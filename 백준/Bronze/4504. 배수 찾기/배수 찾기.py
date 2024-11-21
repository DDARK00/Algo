import sys
input=sys.stdin.readline
n = int(input())

while True:
    k = int(input())
    if k == 0:
        break
    print(f'{k} is{" NOT" if k%n != 0 else""} a multiple of {n}.')