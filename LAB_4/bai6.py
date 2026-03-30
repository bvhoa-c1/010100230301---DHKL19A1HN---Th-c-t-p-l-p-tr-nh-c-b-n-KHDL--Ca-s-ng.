n = int(input("Nhập n: "))
s = str(n)
arms = sum(int(d)**len(s) for d in s)
if arms == n:
    print("Đúng")
else:
    print("Sai")
