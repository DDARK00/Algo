a, b, c = map(int, input().split())
A, B, C = map(int, input().split())

aa = A-a if A-a>0 else 0
bb = B-b if B-b>0 else 0
cc = C-c if C-c>0 else 0
print(aa+bb+cc)