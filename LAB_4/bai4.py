tong = 0
dem = 0
max_val = None

while True:
    num = float(input("Nhập số (0 để dừng): "))
    if num == 0:
        break
    tong += num
    dem += 1
    if max_val is None or num > max_val:
        max_val = num

print(f"Tổng: {tong}, Số lượng: {dem}, Số lớn nhất: {max_val}")