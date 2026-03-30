n = int(input("Nhập n: "))
max_uoc = 0
so_max = 0

for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count > max_uoc:
        max_uoc = count
        so_max = i

print("Số:", so_max, "Có", max_uoc, "ước")