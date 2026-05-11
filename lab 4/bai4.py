tong = 0
dem = 0
max_so = None

while True:
    x = int(input("Nhập số (0 để dừng): "))

    if x == 0:
        break

    tong += x
    dem += 1

    if max_so is None or x > max_so:
        max_so = x

print("Tổng:", tong)
print("Số lượng:", dem)
print("Số lớn nhất:", max_so)