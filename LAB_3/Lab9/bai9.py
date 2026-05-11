n = int(input("Nhập n: "))
max_uoc = 0
number = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count > max_uoc:
        max_uoc = count
        number = i
print("Số có nhiều ước nhất:", number)
print("Số lượng ước:", max_uoc)