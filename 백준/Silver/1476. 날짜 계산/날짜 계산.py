import sys
input = sys.stdin.readline
e, s, m = map(int, input().split())

cnt = 1
one, two, three = 1,1,1
while True:
    if one == e and two == s and m == three:
        break
    cnt+=1
    one = one+1 if one<15 else 1
    two = two+1 if two<28 else 1
    three = three+1 if three<19 else 1
print(cnt)