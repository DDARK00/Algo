import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    one=int(a)*int(b)
    two=""
    b = "1"*max(len(a)-len(b),0)+b
    a = "1"*max(len(b)-len(a),0)+a
 
    for idx, num in enumerate(b):
        two += str(int(num)*int(a[idx]))
    if one == int(two):
        print(1)
    else:
        print(0)