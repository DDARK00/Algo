for _ in range(int(input())):
    a, b = map(int, input().split())
    # 내선 1->43
    # 외선 43->1
    if a<b:
        inner = b-a
        outer = a-b+43
    else:
        inner = b-a+43
        outer = a-b

    if inner<outer:
        print("Inner circle line")
    elif inner==outer:
        print("Same")
    else:
        print("Outer circle line")