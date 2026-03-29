n = int(input("Nhập n: "))

max_sum = 0
so_max = 0

for i in range(1, n + 1):
    s = 0
    for digit in str(i):
        s += int(digit)
    if s > max_sum:
        max_sum = s
        so_max = i

print("Số cần tìm =", so_max)