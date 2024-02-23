# n = int(input())
#
#
# def encdec(n):
#     return n ^ 1004
#
#
# print(encdec(n))
#
# for i in range(5):
#     rst = 1 << i
#     print(f'Loop {i + 1} : {bin(rst)} 출력 # {rst}')
#     print('Loop %d : %s 출력 # %d' % (i + 1, bin(rst), rst))
#
#     n = i
#     if i & (1 << n):
#         print(i, 'n번비트는 1')
T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())


    def chk(n, m):
        for i in range(n):
            if not m & (1 << i):
                return False

        return True


    if chk(n,m):
        print(f'#{t} ON')
    else:
        print(f'#{t} OFF')
