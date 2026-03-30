n = input("Nhập số: ")

tong = 0
tich = 1

for digit in n:
    tong += int(digit)
    tich *= int(digit)

dao = n[::-1]

print("Tổng:", tong)
print("Tích:", tich)
print("Đảo:", dao)