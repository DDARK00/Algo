txt = input()


target = ["U","C","P","C"]


idx = 0

s = ""
for c in txt :
    if c ==target[idx]:
        idx+=1
        s+=c
    if idx>3:
        break

if s == "UCPC":
    print('I love UCPC')
else:
    print('I hate UCPC')