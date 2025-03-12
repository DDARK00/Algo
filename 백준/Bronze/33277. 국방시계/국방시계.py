import sys
input=sys.stdin.readline

a, b = map(int, input().split())
time = (b/a)*(24*60)
print(f'{("0"+str(int(time//60)))[-2:]}:{("0"+str(int(time%60)))[-2:]}')