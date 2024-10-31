s=input()
key=ord(s[0])^ord("C")
for c in s: 
    print(chr(ord(c)^key),end="")