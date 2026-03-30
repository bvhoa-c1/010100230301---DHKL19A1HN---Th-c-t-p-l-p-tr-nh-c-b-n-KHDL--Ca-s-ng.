n = int(input("Nhập n: "))
dem = 0

for i in range(1, n + 1):
    tong = 0
    temp = i
    while temp > 0:
        tong += temp % 10
        temp //= 10

    if tong % 2 == 0:
        dem += 1

print("Số lượng =", dem)