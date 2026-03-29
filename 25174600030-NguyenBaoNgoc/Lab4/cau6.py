n = int(input("Nhập n: "))

temp = n
k = 0

# Đếm số chữ số
while temp > 0:
    k += 1
    temp //= 10

temp = n
tong = 0

# Tính tổng lũy thừa
while temp > 0:
    digit = temp % 10
    tong += digit ** k
    temp //= 10

if tong == n:
    print(n, "là số Armstrong")
else:
    print(n, "không phải số Armstrong")