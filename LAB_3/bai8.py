# Bài 8: Tìm số có tổng chữ số lớn nhất trong [1, n]

n = int(input("Nhập n: "))
max_sum = 0
max_num = 1
for i in range(1, n+1):
    digit_sum = 0
    temp = i
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum > max_sum:
        max_sum = digit_sum
        max_num = i

print(f"Số có tổng chữ số lớn nhất là {max_num} (tổng = {max_sum})")
