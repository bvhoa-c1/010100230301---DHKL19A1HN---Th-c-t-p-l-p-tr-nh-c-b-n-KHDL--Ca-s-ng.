# Bài 6: Kiểm tra số Armstrong
n = int(input("Nhập n: "))
s = str(n)
length = len(s)
arm = sum(int(d) ** length for d in s)
if arm == n:
    print("Là số Armstrong")
else:
    print("Không phải số Armstrong")
