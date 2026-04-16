import sys
input=sys.stdin.readline

data=[]
length=[0]*91
while True:
    s=input().split()

    if s==[]:
        break
    for idx, word in enumerate(s):
        length[idx]=max(length[idx],len(word))
    data.append(s)

for s in data:
    for i in range(len(s)-1):
        print(s[i]+' '*(length[i]+1-len(s[i])), end="")
    print(s[-1])