s = input()

ar= []
for i in range(len(s)):
    ar.append(s[i:])

ar.sort()

for a in ar:
    print(a)
    # 실버4에 있는 이유가 뭘까 이거