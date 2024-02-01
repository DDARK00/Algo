T = int(input())
for _ in range(T):
    lst = []
    in_ps = input()

    len(in_ps)

    is_ps = True

    for ps in in_ps:
        if ps == "(":
            lst.append("(")
        if ps == ")":
            if lst:
                pull = lst.pop()
            else:
                print('NO')
                is_ps = False
                break

    if is_ps and not lst:
        print('YES')
    elif lst :
        print("NO")
    # elif
