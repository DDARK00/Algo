T = int(input())

idx = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for t in range(1, T + 1):
    n, m = map(int, input().split())
    # 세로크기 n  가로크기 m

    # 스캐너는 암호코드 1개가 포함된 직사각형 배열을 읽는다.
    # 암호코드에서 숫자 하나는 7개의 비트로 암호화되어 주어진다. 따라서 암호코드의 가로 길이는 56이다.

    passwordplate = []
    for _ in range(n):
        passwordplate.append(input())
    # 패스워드 덩어리

    password = None
    # 모든 패스워드는 7번째 숫자가 1임(마지막 숫자)
    for i in range(n):
        for j in range(m - 1, 56, -1):
            # print(i,j)
            if passwordplate[i][j] == '1':
                password = passwordplate[i][j - 55:j + 1]
                # print(i, j)
                break

        if password:
            # print(i, j)
            break

    # 탐색한 곳 -> 처음으로 나온 암호 문장의 맨 마지막 글자
    # print(password)

    pass_lst = []
    for i in range(8):
        pass_lst.append(password[i * 7:i * 7 + 7])
    dec_pass = []
    # print(pass_lst)

    for pas in pass_lst:
        dec_pass.append(idx.index(pas))
        # 비정상적인 암호코드(가로 길이가 56이 아닌 경우, 아래 규칙대로 해독할 수 없는 경우)는 주어지지 않는다.

    # print(dec_pass)

    # 2. 올바른 암호코드는 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수가 되어야 한다.

    osum = 0
    esum = 0
    for i in range(1, 9):
        if i % 2 == 0:
            esum += dec_pass[i - 1]
        else:
            osum += dec_pass[i - 1]
    ssum = osum * 3 + esum

    if not ssum % 10:
        # 나머지가 0이면
        print(f'#{t} {esum + osum}')
    else:
        print(f'#{t} 0')

