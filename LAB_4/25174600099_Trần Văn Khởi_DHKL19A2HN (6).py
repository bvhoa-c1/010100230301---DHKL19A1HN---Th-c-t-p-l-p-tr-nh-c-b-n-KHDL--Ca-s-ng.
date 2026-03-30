n = input("Nhập số: ")
k = len(n)

tong = 0
for digit in n:
    tong += int(digit) ** k

if tong == int(n):
    print("Là số Armstrong")
else:
    print("Không phải")