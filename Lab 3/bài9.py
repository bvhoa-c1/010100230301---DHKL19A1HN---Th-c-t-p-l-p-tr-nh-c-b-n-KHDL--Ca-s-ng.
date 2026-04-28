n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải > 0, vui lòng nhập lại: "))

max_divisors = 0
so_max = 1

for i in range(1, n + 1):

    count_div = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count_div += 1
    
    
    if count_div > max_divisors:
        max_divisors = count_div
        so_max = i

print("Số có nhiều ước nhất trong khoảng [1,", n, "] là:", so_max)
print("Số lượng ước =", max_divisors)