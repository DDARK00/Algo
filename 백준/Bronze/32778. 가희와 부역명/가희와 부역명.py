s = input()
if "(" in s:
    a, b = s.split("(")
else:
    a, b = s, ""
print(a)
print(b[:-1] or "-")