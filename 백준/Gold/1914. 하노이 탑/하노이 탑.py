def hanoi(number, fr, to, sub):

    if number == 1:

        print(fr, to)

    else:

        hanoi(number-1, fr, sub, to)

        print(fr, to)

        hanoi(number-1, sub, to, fr)

        

n = int(input())

print(2**n-1)

if n<=20:

    hanoi(n,1,3,2)

# n번을 제외한 기둥을 2번에 옮기기 -> n-1번을 제외한 기둥 3번에 옮기기

# 한방향 쌓고 반대방향 쌓고 1번 밀기