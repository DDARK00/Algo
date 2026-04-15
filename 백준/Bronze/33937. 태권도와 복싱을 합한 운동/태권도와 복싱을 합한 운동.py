import sys
input=sys.stdin.readline

s1=input().rstrip()
s2=input().rstrip()

temp=""
head=""
tail=""
s1_ok=False
for i in range(len(s1)):
    if s1[i] not in "aeiou" and s1_ok:
        head=temp
        temp=""
        break
    temp+=s1[i]
    if s1[i] in "aeiou":
        s1_ok=True
if temp:
    print("no such exercise")
    exit()
s2_ok=False
for i in range(len(s2)):
    if s2[i] not in "aeiou" and s2_ok:
        tail=temp
        temp=""
        break
    temp+=s2[i]
    if s2[i] in "aeiou":
        s2_ok=True
if temp:
    print("no such exercise")
    exit()
print(head+tail)