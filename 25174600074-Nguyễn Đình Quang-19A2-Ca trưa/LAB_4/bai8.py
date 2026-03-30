n = int(input("Nhập n: "))
tong = 0
tich = 1
dao = 0

while n > 0:
    d = n % 10
    tong += d
    tich *= d
    dao = dao * 10 + d
    n //= 10

print("Tổng:", tong)
print("Tích:", tich)
print("Đảo:", dao)