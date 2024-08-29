import sys
input= sys.stdin.readline

n=int(input())

s=set()

for _ in range(n):
    co = input()
    if co.startswith("add"):
        c, x = co.split()
        s.add(x)
        
    elif co.startswith("remove"):
        c, x= co.split()
        s.discard(x)
        
    elif co.startswith("check"):
        c, x = co.split()
        if x in s:
            print(1)
        else:
            print(0)
        
    elif co.startswith("toggle"):
        c, x = co.split()
        if x in s:
            s.discard(x)
        else:
            s.add(x)
            
    elif co.startswith("all"):
        s.clear()
        s.update({'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'})
        
    else:
        s.clear()