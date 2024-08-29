s = input()
a = input()

word = ""
for c in s:
    # 파이썬정ㅠ규식어떻게씀
    if not c.isdigit():
        word+=c
if a in word:
    print(1)
else:
    print(0)