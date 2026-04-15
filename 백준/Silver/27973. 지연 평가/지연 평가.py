import sys
input=sys.stdin.readline

target=1
added=0
multiplied=1
for _ in range(int(input())):
    cmd = input().rstrip()
    cmd,k=cmd[0],cmd[1:]
    if cmd == '0':
        added+=int(k)
    elif cmd == '1':
        multiplied*=int(k)
        added*=int(k)
    elif cmd == '2':
        target+=int(k)
    else:
        print(target*multiplied+added)