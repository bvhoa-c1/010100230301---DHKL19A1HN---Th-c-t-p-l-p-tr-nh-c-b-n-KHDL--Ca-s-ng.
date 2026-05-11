tong = 0
count = 0
max_num = None
while True:
    n = int(input("Nhập số (0 để dừng): "))
    if n == 0:
        break
    tong += n
    count += 1
    if max_num is None or n > max_num:
        max_num = n
print("Tổng:", tong)
print("Số lượng:", count)
print("Số lớn nhất:", max_num)