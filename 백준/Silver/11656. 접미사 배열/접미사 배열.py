s = input()

ar= []
for i in range(len(s)):
    ar.append(s[i:])

ar.sort()

for a in ar:
    print(a)