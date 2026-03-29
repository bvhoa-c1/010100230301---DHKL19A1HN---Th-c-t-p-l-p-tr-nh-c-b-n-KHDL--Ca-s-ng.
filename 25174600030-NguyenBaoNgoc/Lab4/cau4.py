tong = 0
dem = 0
max_so = None

while True:
    n = int(input("Nhập số (0 để dừng): "))
    
    if n == 0:
        break
    
    tong += n
    dem += 1
    
    if max_so is None or n > max_so:
        max_so = n

print("Tổng:", tong)
print("Số lượng:", dem)
print("Số lớn nhất:", max_so)