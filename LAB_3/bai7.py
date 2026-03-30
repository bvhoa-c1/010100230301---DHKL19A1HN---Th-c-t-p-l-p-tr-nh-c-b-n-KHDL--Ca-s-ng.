# Bài 7: Đếm số lượng số trong [1, n] có tổng chữ số là số chẵn

n = int(input("Nhập n: "))
count = 0
for i in range(1, n+1):
    digit_sum = 0
    temp = i
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum % 2 == 0:
        count += 1

print(f"Số lượng số có tổng chữ số chẵn: {count}")
