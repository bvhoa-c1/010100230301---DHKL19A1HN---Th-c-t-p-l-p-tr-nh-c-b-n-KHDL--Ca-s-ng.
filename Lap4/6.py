n = int(input("Nhập n: "))
temp = n
tong = 0
while temp > 0:
    digit = temp % 10
    tong += digit ** 3
    temp //= 10
if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải")