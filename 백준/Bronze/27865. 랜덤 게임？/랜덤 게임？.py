import sys
input=sys.stdin.readline

n = int(input())
while True:
    print(f"? {n}")
    sys.stdout.flush()
    ans = input().rstrip()
    if ans=="Y":
        print(f'! {n}')
        break