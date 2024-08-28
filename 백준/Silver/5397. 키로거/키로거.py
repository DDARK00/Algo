import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    s = input().rstrip()
    head = []
    tail = []
    # write right side
    for c in s:
        if c == "<":
            if head:
                tail.append(head.pop())
        elif c == ">":
            if tail:
                head.append(tail.pop())
        elif c == "-":
            if head:
                head.pop()
        else:
            head.append(c)
    tail.reverse()
    print("".join(head),end="")
    print("".join(tail))