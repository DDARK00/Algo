n = int(input())

tree = {}
for _ in range(n):
    p, c1, c2 = input().split()
    tree[p] = []
    tree[p].append(c1)
    tree[p].append(c2)


# 전위 t l r
# print(tree)


def pre(p):
    print(p, end="")

    c1, c2 = tree[p]
    if c1 != ".":
        pre(c1)
    if c2 != ".":
        pre(c2)


pre("A")
print()


def ind(p):
    c1, c2 = tree[p]
    if c1 != ".":
        ind(c1)
    print(p, end="")
    if c2 != ".":
        ind(c2)


ind("A")
print()


def pos(p):
    c1, c2 = tree[p]
    if c1 != ".":
        pos(c1)
    if c2 != ".":
        pos(c2)
    print(p, end="")

pos("A")