# Bài 9: Tìm số có nhiều ước nhất trong [1, n]

n = int(input("Nhập n: "))
max_divisors = 0
num_max = 1
for i in range(1, n+1):
    count_div = 0
    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            count_div += 1
            if j != i//j:
                count_div += 1
    if count_div > max_divisors:
        max_divisors = count_div
        num_max = i

print(f"Số có nhiều ước nhất là {num_max} ({max_divisors} ước)")
