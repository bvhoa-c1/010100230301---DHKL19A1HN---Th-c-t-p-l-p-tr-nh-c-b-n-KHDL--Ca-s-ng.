n = int(input("Nhập n: "))
s = str(n)
arm = sum(int(d)**len(s) for d in s)
if arm == n:
    print("Là số Armstrong")
else:
    print("Không phải số Armstrong")
