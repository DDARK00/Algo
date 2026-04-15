a,b=0,0
for c in input():a+=']}).({['.find(c)-3if c in '({[]})'else min(0,b:=max(a,b))
print(b)