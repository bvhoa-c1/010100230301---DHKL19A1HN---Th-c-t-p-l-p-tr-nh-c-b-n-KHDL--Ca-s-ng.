n = int(input("Nhập n: "))

tong = 0
tich = 1
dao = 0

temp = n

while temp > 0:
    digit = temp % 10
    tong += digit
    tich *= digit
    dao = dao * 10 + digit
    temp //= 10

print("Tổng chữ số:", tong)
print("Tích chữ số:", tich)
print("Số đảo:", dao)