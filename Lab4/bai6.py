n = int(input("Nhập n: "))
original = n
tong = 0

while n > 0:
    digit = n % 10
    tong += digit ** 3
    n //= 10

if tong == original:
    print("Là số Armstrong")
else:
    print("Không phải")