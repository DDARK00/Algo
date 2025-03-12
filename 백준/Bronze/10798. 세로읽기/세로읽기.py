lst = []
for _ in range(5):
    s = input()
    s+=" "*(15-len(s))
    lst.append(s)
lst = map("".join,zip(*lst))
s = "".join(lst)
print(s.replace(" ",""))