total = 0
count = 0
max_val = -float('inf')

while True:
    num = float(input("Nhập số (0 để dừng): "))
    if num == 0:
        break
    total += num
    count += 1
    if num > max_val:
        max_val = num

if count > 0:
    print(total)
    print(count)
    print(max_val)