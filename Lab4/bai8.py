n = int(input("Nhập n: "))
tong = 0
tich = 1
dao = 0

while n > 0:
    digit = n % 10
    tong += digit
    tich *= digit
    dao = dao * 10 + digit
    n //= 10

print("Tổng:", tong)
print("Tích:", tich)
print("Số đảo:", dao)