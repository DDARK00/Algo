s = input()

ans = ""
for c in s:
    if c.isupper():
        ans+=c.lower()
    else:
        ans+=c.upper()

print(ans)