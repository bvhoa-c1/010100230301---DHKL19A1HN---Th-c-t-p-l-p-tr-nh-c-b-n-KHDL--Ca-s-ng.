n = int(input("Nhập n: "))
max_sum = 0
so_max = 0
for i in range(1, n+1):
    tong = sum(int(d) for d in str(i))
    if tong > max_sum:
        max_sum = tong
        so_max = i
print("Số: ", so_max, "Tổng chữ số: ", max_sum)