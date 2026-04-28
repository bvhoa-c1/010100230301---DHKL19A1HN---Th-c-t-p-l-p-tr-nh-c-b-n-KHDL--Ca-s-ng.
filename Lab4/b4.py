tong = 0
dem = 0
max_num = None 
while True:
    n = int(input("Nhập số (0 để dừng): "))
    if n == 0:
        break
    tong += n
    dem += 1
    if max_num is None or n > max_num:
        max_num = n
print("Tổng:", tong)
print("số lượng:", dem)
print("Max:", max_num)