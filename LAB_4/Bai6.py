n = int(input("Nhập n: "))
temp = n
tong = 0
while temp > 0:
    so = temp % 10
    tong += so ** 3
    temp //= 10
if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải")