total = 0
count = 0
max_num = None
while True:
    num = int(input("Nhập số (0 để dừng): "))
    if num == 0:
        break
    total += num
    count += 1
    if max_num is None or num > max_num:
        max_num = num
print("Tổng các số:", total)
print("Số lượng số:", count)
print("Số lớn nhất:", max_num)