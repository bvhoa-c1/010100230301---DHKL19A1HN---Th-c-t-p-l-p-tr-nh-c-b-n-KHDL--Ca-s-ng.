total = 0
count = 0
max_num = float('-inf')
while True:
    num = int(input("Nhập số (0 để dừng): "))
    if num == 0:
        break
    total += num
    count += 1
    if num > max_num:
        max_num = num
print(f"Tổng: {total}")
print(f"Số lượng: {count}")
print(f"Số lớn nhất: {max_num}")
