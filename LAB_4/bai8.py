n = int(input("Nhập n: "))
tong = 0
tich = 1
dao = 0
temp = n
while temp > 0:
    dv = temp % 10
    tong += dv
    tich *= dv
    dao = dao * 10 + dv
    temp //= 10
print(f"Tổng: {tong}, Tích: {tich}, Số đảo: {dao}")