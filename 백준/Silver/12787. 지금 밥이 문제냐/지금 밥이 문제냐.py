import sys
input=sys.stdin.readline

for _ in range(int(input())):
    i, s=input().split()
    if i=='1':
        p='0b'
        for k in map(int,s.split('.')):
            p+=('0000000'+bin(k)[2:])[-8:]
        print(int(p,2))
    else:
        target=('0'*64+bin(int(s))[2:])[-64:]
        l=['']*8
        for i in range(8):
            l[i]=str(int(target[i*8:i*8+8],2))
        print('.'.join(l))