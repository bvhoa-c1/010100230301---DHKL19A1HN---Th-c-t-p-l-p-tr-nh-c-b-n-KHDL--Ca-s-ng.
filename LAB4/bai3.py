# Bài 3: Tìm ước số lớn nhất của n (khác n)
n = int(input("Nhập n: "))
max_div = 1
i = 2
while i * i <= n:
    if n % i == 0:
        max_div = max(max_div, i, n // i)
    i += 1
print(f"Ước số lớn nhất khác {n} là {max_div}")
