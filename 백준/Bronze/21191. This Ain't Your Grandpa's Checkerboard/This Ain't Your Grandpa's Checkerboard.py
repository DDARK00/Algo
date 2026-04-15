import sys
input=sys.stdin.readline

n=int(input())
lst = []
correct = 1
for _ in range(n):
    line = input().rstrip()
    ren=0
    before=""
    cnt = {"B":0, "W":0}
    for i in range(n):
        cnt[line[i]]+=1
        if before == line[i]:
            ren+=1
        else:
            before = line[i]
            ren=1
        if ren==3:
            correct=0
            break
    if cnt["B"] != n//2 or cnt["W"] != n//2:
        correct = 0
    if not correct:
        break
    lst.append(line)

if correct:
    for i in range(n):
        ren=0
        before=""
        cnt={"B":0,"W":0}
        for j in range(n):
            cnt[lst[j][i]]+=1
            if before == lst[j][i]:
                ren+=1
            else:
                before = lst[j][i]
                ren=1
            if ren==3:
                correct=0
                break
        if cnt["B"] != n//2 or cnt["W"] != n//2:
            correct = 0
        if not correct:
            break
print(correct)