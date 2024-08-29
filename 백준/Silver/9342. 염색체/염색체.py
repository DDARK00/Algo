import re

pattern = re.compile("^[A-F]?A+F+C+[A-F]?$")

for  _ in range(int(input())):
    s = input()
    if pattern.match(s):
        print("Infected!")
    else:
        print("Good")