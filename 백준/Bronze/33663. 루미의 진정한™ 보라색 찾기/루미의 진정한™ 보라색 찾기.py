hi, hj = map(int, input().split())
si, sj = map(int, input().split())
vi, vj = map(int, input().split())
r, g, b = map(int, input().split())
 
M = max(r,g,b)
m = min(r,g,b)
 
V = M
S = 255*((V-m)/V)
if V == r:
    H = (60*(g-b))/(r-m)
elif V == g:
    H = 120+(60*(b-r))/(g-m)
else:
    H = 240+(60*(r-g))/(b-m)
H = (H+360)%360
 
if vi<=V<=vj and si<=S<=sj and hi<=H<=hj:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")