import sys
input=sys.stdin.readline

s=input().rstrip();

def solve(s):
    depth = 0
    st = []
    chk = []
    for c in s:
        if c == ")": # 2
            if not chk or chk[-1] != "(":
                return 0
            chk.pop()
            temp = 2
            while st and st[-1][1]>=depth:
                if st[-1][1] == depth:
                    temp += st[-1][2]
                else:
                    temp *= st[-1][2]
                st.pop()
            st.append((2,depth,temp)) # origin, depth, value
            depth -=1
            
        elif c == "]" : # 3
            if not chk or chk[-1] != "[":
                return 0
            chk.pop()
            temp = 3
            while st and st[-1][1]>=depth:
                if st[-1][1] == depth:
                    temp += st[-1][2]
                else:
                    temp *= st[-1][2]
                st.pop()
            st.append((3,depth,temp))
            depth -=1

        elif c == "(" : # 2
            chk.append(c)
            depth +=1
        else: # 3
            chk.append(c)
            depth +=1
            
    # print(st)
    if chk:
        return 0
    return st[-1][2]
print(solve(s))