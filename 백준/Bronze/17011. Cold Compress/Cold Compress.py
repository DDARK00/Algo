import sys
input=sys.stdin.readline

for _ in range(int(input())):
    line=input().rstrip()
    s=""
    b=line[0]
    cnt=0
    for c in line:
        if b==c:
            cnt+=1
        else:
            s+= f'{cnt} {b} '
            b=c
            cnt=1
    s+= f'{cnt} {b} '

    print(s)