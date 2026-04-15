import sys, datetime
input=sys.stdin.readline

no=input().rstrip()

local=no[:6]
yy,mm,dd=map(int,(no[6:10],no[10:12],no[12:14]))
order=no[14:17]
chk=no[17:]

try:
    datetime.datetime(yy,mm,dd)
    int(order)
    if yy<1900 or yy>2011 or order=='000':
        raise Exception()

    for _ in range(int(input())):
        if input().rstrip()==local:
            x=0
            for i in range(17):
                x+=int(no[i])*(2**(17-i))
                x%=11
            if (chk=='X' and (12-x)%11 !=10):
                raise Exception()
            elif chk!='X'and (int(chk) != (12-x)%11):
                raise Exception()
            print('M' if int(order)%2 else 'F')
            exit()
    raise Exception()

except Exception:
    print("I")