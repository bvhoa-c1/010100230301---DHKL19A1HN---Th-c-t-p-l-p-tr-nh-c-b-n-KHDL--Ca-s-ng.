tong = 0
count = 0
max_val = None
while True:
    n = int(input("Nhập số (0 để dừng): "))
    if n == 0:
        break

    tong += n
    count += 1
    if max_val is None or n > max_val:
       max_val = n

print("Tổng:", tong)
print("Số lượng:", count)
print("Max:", max_val)