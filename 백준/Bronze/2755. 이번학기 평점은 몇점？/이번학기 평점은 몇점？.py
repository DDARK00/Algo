import sys
score={
    "A+": 430, "A0": 400, "A-": 370,
    "B+": 330, "B0": 300, "B-": 270,
    "C+": 230, "C0": 200, "C-": 170,
    "D+": 130, "D0": 100, "D-": 70,
    "F": 0
}

gx = 0
gy = 0

for _ in range(int(sys.stdin.readline())):
    _, c, g = sys.stdin.readline().split()
    grade_score = score[g]
    gx+=int(c)
    gy+=score[g]*int(c)

ans=gy//gx
ans += 1 if gy/gx%1>=0.5 else 0
ans=ans/100.0
print(f"{ans:.2f}")