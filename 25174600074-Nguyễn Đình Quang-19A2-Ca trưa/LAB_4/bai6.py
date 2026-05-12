n = input("Nhập số: ")
k = len(n)
tong = 0

for i in n:
    tong += int(i) ** k

if tong == int(n):
    print("Là số Armstrong")
else:
    print("Không phải")