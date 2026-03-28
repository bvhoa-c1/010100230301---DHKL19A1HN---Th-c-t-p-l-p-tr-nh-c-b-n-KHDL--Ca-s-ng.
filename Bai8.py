n = int(input("Nhập n: "))
temp = n
tong = 0
tich = 1
dao = 0
while temp > 0:
    so = temp % 10
    tong += so
    tich *= so
    dao = dao * 10 + so
    temp //= 10
print("Tổng:", tong)
print("Tích:", tich)
print("Số đảo:", dao)