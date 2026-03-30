tong = 0
dem = 0
max_so = float('-inf')
print("Nhập các số (0 để dừng):")
while True:
    x = int(input())
    if x == 0:
        break
    tong += x
    dem += 1
    if x > max_so:
        max_so = x
print("Tổng:", tong)
print("Số lượng:", dem)
print("Số lớn nhất:", max_so)
