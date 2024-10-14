import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == "EOI":
        break
    s = s.lower()
    if "nemo" in s:
        print("Found")
    else:
        print("Missing")