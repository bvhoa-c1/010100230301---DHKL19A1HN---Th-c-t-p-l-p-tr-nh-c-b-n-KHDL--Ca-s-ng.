tong = 0
dem = 0
max_val = None

while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    tong += x
    dem += 1
    if max_val is None or x > max_val:
        max_val = x

print("Tổng:", tong)
print("Số lượng:", dem)
print("Max:", max_val)